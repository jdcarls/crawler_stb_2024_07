from bs4 import BeautifulSoup as Bs
import requests
import pandas as pd
import re
import datetime
import uuid
import time

# FUNCTION TO PRINT FIRST 30 ENTRIES INCLUDING NUMBER/ORDER, TITLE, POINTS AND COMMENTS


def fetch_data():
    website = "https://news.ycombinator.com/"
    # Use of requests library to fetch web content (stored in website_data)
    website_data = requests.get(website)
    # Creating a Bs object for parsed html using Python's built-in html parser
    # Using .txt since response will be unicode string as we are fetching html content
    parsed_html = Bs(website_data.text, 'html.parser')
    website_table_rows = parsed_html.select('.athing')[:30]

    # empty list, later to be appended using dict key value pairs: order, title, points, comments
    results = []
    # Stored first 30 entries in website_table_rows above
    # Now looping over the 30 entries using a for loop keeping track of the order using enumerate function

    for i, single_row in enumerate(website_table_rows):
        html_data_title = single_row.select_one('.titleline')
        # Using .get_text() method below ignores html tags and just extracts text.
        # Checking also that html_data_title is not None / title_text will be the value for the dictionary key 'title'
        title_text = html_data_title.get_text() if html_data_title else 'Title is missing'

        # We find score and number of comments in the 'subtext' class of the html
        subtext = single_row.find_next_sibling()
        # Now we are specifically looking for '.score' using a conditional

        if subtext:
            score_subline = subtext.select_one('.score')
            # we are extracting only text using get_text() on the value stored in score_subline
            score_text = score_subline.get_text() if score_subline else '0 points'
            # we are looking for the href tag and in case it has changed, it will nevertheless be identified correctly
            matching_link = subtext.select('a[href*="item?id="]')
            comments_subline = matching_link[0] if matching_link else None
            comments_text = comments_subline.get_text().strip() \
                if comments_subline and 'comment' in comments_subline.get_text() else '0 comments'
        else:
            score_text = '0 points'
            comments_text = '0 comments'

        # Creating dictionary key-value pairs for order, title, points,comments that are saved in the dictionary result.
        # Then appending results list
        result = {

            'order': i+1,
            'title': title_text,
            'points': score_text,
            'comments': comments_text
        }

        results.append(result)

    return results


# CREATING DATA FRAME FOR FILTERED DATA (The filter data function takes in the data from the fetch_data function)

def filter_data(data):
    # Storing start time for runtime calculation
    start_time = time.time()

    # Implementation of a unique identifier when running the function
    identifier = str(uuid.uuid4())

    # Now we are converting the returned list of dictionaries from the fetch data function into a data frame.
    df = pd.DataFrame(data)
    # Above we are using the Pandas library to create a DataFrame

    # We need to extract the number of points and comments as number and comments also contain text
    # Here we extract the numeric part of the string, which can be one or more digits - that's why we are using regex d+
    # astype(int) then turns the extracted numerical string information into an integer
    df['points'] = df['points'].str.extract('(\d+)').astype(int)
    df['comments'] = df['comments'].str.extract('(\d+)').astype(int)

    # Set up a new column in the data frame for word count as number of words is part of the filtering criteria
    # We are applying the lambda function to the entries in the title column. The regular expression allows word count
    # without punctuation
    df['title_count_words'] = df['title'].apply(lambda x: len(re.findall(r'\b\w+\b', x)))

    # FILTERING 1: MORE THAN 5 WORDS IN TITLE SORTED BY COMMENTS
    filtered_by_comments_df = df[df['title_count_words'] > 5].sort_values(by='comments', ascending=False)

    # FILTERING 2: LESS THAN OR EQUAL TO 5 WORDS IN TITLE SORTED BY POINTS
    filtered_by_points_df = df[df['title_count_words'] <= 5].sort_values(by='points', ascending=False)

    # Implementation of timestamp and filtering rule for each df
    timestamp = datetime.datetime.now()
    filtered_by_comments_df['timestamp'] = timestamp
    filtered_by_comments_df['filter'] = "More than 5 words in title sorted by comments"

    timestamp = datetime.datetime.now()
    filtered_by_points_df['timestamp'] = timestamp
    filtered_by_points_df['filter'] = "Less than or equal to 5 words in title sorted by points"

    # Implementation of identifier for each df
    filtered_by_comments_df['crawl_id'] = identifier
    filtered_by_points_df['crawl_id'] = identifier

    # Displaying the crawler version
    crawler_version = "V. 1.0"
    filtered_by_comments_df['crawler_version'] = crawler_version
    filtered_by_points_df['crawler_version'] = crawler_version

    # Storing end time of crawl for runtime calculation
    end_time = time.time()

    # Calculation of runtime
    runtime = end_time - start_time

    # Including the runtime in each df
    filtered_by_comments_df['runtime'] = runtime
    filtered_by_points_df['runtime'] = runtime

    # Saving df in to a csv file
    filtered_by_comments_df('filtered_by_comments_df.csv', index=False)
    filtered_by_points_df('filtered_by_points_df.csv', index=False)

    # Returning the filtered df
    return filtered_by_comments_df, filtered_by_points_df


data = fetch_data()
filtered_data = filter_data(data)

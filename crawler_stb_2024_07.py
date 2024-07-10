from bs4 import BeautifulSoup as Bs
import requests
import pandas as pd

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
            # we are looking for the href tag and in case id has changed it will nevertheless be identified correctly
            matching_link = subtext.select('a[href*="item?id="]')
            comments_subline = matching_link[0] if matching_link else None
            comments_text = comments_subline.get_text().strip() \
                if comments_subline and 'comment' in comments_subline.get_text() else '0 comments'
        else:
            score_text = '0 points'
            comments_text = '0 comments'

        # Creating dictionary 'result' for order, title, points, comments. Then appending results list
        result = {

            'order': i+1,
            'title': title_text,
            'points': score_text,
            'comments': comments_text
        }

        results.append(result)

    return results

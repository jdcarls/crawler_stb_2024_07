# Web-Crawler Project - Version 1.0

## Objectives

Using the language that you feel most proficient in, create a web crawler using scraping techniques to extract the first 30 entries from https://news.ycombinator.com/. You'll only care about the number, the title, the points, and the number of comments for each entry.

From there, we want it to be able to perform a couple of filtering operations:

    Filter all previous entries with more than five words in the title ordered by the number of comments first.
    Filter all previous entries with less than or equal to five words in the title ordered by points.

When counting words, consider only the spaced words and exclude any symbols. For instance, the phrase “This is - a self-explained example” should be counted as having 5 words.

The solution should store usage data, including at least the request timestamp and a field to identify the applied filter. You are free to include any additional fields you deem relevant to track user interaction and crawler behavior. The chosen storage mechanism could be a database, cache, or any other suitable tool.

To gain insight into your thought process, please consider including brief documentation explaining the key design decisions you made. This can be formatted in any way you find comfortable, such as an explanatory text file, markdown document, or comments within the code. While an Architectural Decision Record (ADR) format is certainly welcome, exploring alternative formats to explain your decisions is also encouraged.

We will measure the performance of the provided solution and your ability to test the requested operations in the scenarios described above. In addition, we'd love to see the following in your code for extra points:

    Good object-oriented/functional code, avoiding repetition and favoring a consistent organization. You should stick to the semantics of your chosen language and be as consistent as possible.
    Correct usage of version control tools, with a good commit history and incremental software delivery practices.
    Automated testing with any framework or tool of your choice.

    We value candidates who love clean, well-structured code and who can creatively solve problems.
    A ReadMe is always helpful in guiding us through your work.

Please submit the result to a GitHub, GitLab, or Bitbucket repository and send us the URL within 72 hours. Once we receive this information, we'll ask our technical team to review it and let you know about the next steps of the process soon.

---

## Dependencies Used

1. **Requests:** Fetching the web content including html, css, js etc. 
2. **BeautifulSoup4:** Parsing HTML and Data extraction from the fetched website data.
3. **Numpy/Pandas:** Using Pandas (built on top of Numpy) to transform data into a DataFrame.


**Installation: To install the dependencies, use "pip install -r requirements.txt" . This command should work for Linux/MacOS/Windows. Make sure to activate your virtual environment first. **

## Automatically Installed Dependencies

There are also a number of dependencies that are installed automatically as they are required 
by the top-level dependencies mentioned above: **certifi, chardet, urllib3, idna**


## Architectural Decision Records

Architecture decisions are documented in [Architecture Decision Records](adr.md)


## Crawler 
The scraper accesses only https://news.ycombinator.com/ and therefore respects the disallowed pages:
User-Agent: *
Crawl-delay: 30
Disallow: /collapse?
Disallow: /context?
Disallow: /flag?
Disallow: /login
Disallow: /logout
Disallow: /r?
Disallow: /reply?
Disallow: /submitlink?
Disallow: /vote?
Disallow: /x?

Note: These can be obtained through the robots.txt file of the website: https://news.ycombinator.com/robots.txt
<br> <br> **Also, a time interval for scraping of at least 30 seconds should be maintained.**


## Output from Crawler

The output from the crawler is in the form of DataFrames that will be stored in three separate .csv files:

**1. filtered_by_comments_df.csv** <br>
**2. filtered_by_points_df.csv** <br>
**3. combined_data.csv** <br>

Here is an example version of the data displaying order, title, points, comments:

| order | title    | points | comments |
|-------|----------|--------|-----------|
| 1     | title 1  |  15    | 10        |
| 2     | title 2  |  20    | 5         |
| ...   |  ...     |  ...   | ...       |


**Note: The other columns that are part of the df are: word count, timestamp, applied filter, crawl id, version and runtime.**

## Tests

There are two tests included in the test_crawler_2024_07_stackb.py file for the fetch_data function and the filter_data 
function. 



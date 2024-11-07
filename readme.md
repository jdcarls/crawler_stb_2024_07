# Web-Crawler Project - Version 1.0


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



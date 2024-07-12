
# ARCHITECTURAL DECISION RECORD (ADR)

### ADR 1: Using the library 'requests' to fetch website data

**Decision:** Use of `requests` library to fetch data from  https://news.ycombinator.com/

**Reasoning:** To retrieve data from the website, a tool for making http requests was needed. In the context of using
Python, the requests library is the standard for making http requests.  

**Alternatives:** urllib - may lack user friendliness/less intuitive ; http.client - less efficient in terms of amount of code required
httplib2 - also needs more lines of code and not as intuitive as the requests library


### ADR 2: Use of BeautifulSoup4

**Decision:** Using `bs4` to parse html

**Reasoning:** bs4 uses the built-in parser library. So bs4 sits on top of the parser.

**Alternatives:** Other parsers can also be used with bs4 such as lxml. However, for this project the built- in parser was sufficient. 


### ADR 4: Storing scraped data: DataFrames & CSV

**Decision:** Storing data in .csv files using pandas.DataFrame

**Reasoning:** Pandas provides the dataframe object, which is a two-dimensional table (columns, rows). The data was 
stored as .csv file. This file can also be opened with other tools such as text editors, Excel, R - so it is not only
limited to Python. <br> 

CSV files were preferred as a means of storage as they can be directly created from pandas DataFrames. So no databse was neeeded.
Pandas can also be used for further functions when handling CSV data for analysis or transformation.

**Alternatives:** Although there are more robust alternatives such as relational databases (PostgreSQL or NoSQL),
for the purpose of this project, using CSV files was most intuitive and most likely a very suitable
solution for the relatively simple use-case of the project. 


### ADR 5: Implementing two separate crawler functions

**Decision:** In the crawler file there are two separate functions, one that includes fetching and parsing the data and 
the filter function was used to process data further in accordance with the filtering criteria. 

**Reasoning:** There are several advantages of having these two separate functions:

1. Only the fetch function makes server requests. This reduces the load on the server.
2. If the website structure changes, only the fetch function needs to be updated. This improves the structural aspects of
   the functions and facilitates code maintenance. 
3. Also, the two functions can be tested separately. 

**Alternatives:** Another approach would have been to have just one function handle all the processes. However, this would
be a much less organized approach as it the code structure suffers due to a lack of modularity, which increases
the complexity making updates and testing more difficult. 




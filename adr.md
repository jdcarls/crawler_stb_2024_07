
# ARCHITECTURAL DECISION RECORD (ADR)

### ADR 1: Using the library 'requests' to fetch website data

**Decision:** Use of `requests` library to fetch data from  https://news.ycombinator.com/

**Reasoning:** To retrieve data from the website, a tool for making http requests was needed. In the context of using
Python, the `requests` library is the standard for making http requests.  

**Alternatives:** **urllib** - may lack user friendliness/less intuitive ; **http.client** - less efficient in terms of amount of code required
**httplib2** - also needs more lines of code and not as intuitive as the `requests` library


when i get to pandas and data-frame, explain that the data-frame helps to reduce
number of requests so that ip address is not blocked and server not overloaded with requests.






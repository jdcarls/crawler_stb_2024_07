import unittest
import pandas as pd
from crawler_stb_2024_07 import fetch_data, filter_data
from unittest.mock import patch, MagicMock


"""
Note:   Testing the fetch_data function here is more in line with the idea of an integration test as the test depends
        on an external server request. 

        Testing the current version of the crawler for the fetch_data function is dependent on whether the site has
        changed or not. In case changes have been made to the website, the fetch_data function needs to be revisited
        and updated accordingly.
         
        So it makes sense to devise the test for the fetch_data function as an integration test. 
        
        The filter_data function on the other hand simply relies on the returned output from the fetch_data function
        and therefore it can be tested more in isolation - the function is more contained as it manipulates data that
        has already been fetched.  """


# TESTING FETCH_DATA FUNCTION

# ---Test Expectations---
# Testing whether the fetch_data function returns 30 entries. Does the function return the expected no of entries.
# Testing that each item in returned list is a dictionary ('order', 'title', 'points', 'comments')
# Testing that the order of the 30 entries is in sequence from 1 to 30.So data should be fetched and ordered as expected


class TestFetchData(unittest.TestCase):
    def test_fetch_data(self):
        results = fetch_data()
        # Validating results is a list
        self.assertIsInstance(results, list)
        # Validating there are 30 result entries
        self.assertEqual(len(results), 30)

        # Now we are testing the data-type of the result entries (dictionary)
        # And we are checking the dictionary keys
        for result in results:
            self.assertIsInstance(result, dict)
            self.assertIn('order', result)
            self.assertIn('title', result)
            self.assertIn('points', result)
            self.assertIn('comments', result)

        # Asserting on the order of the results
        orders = [result['order'] for result in results]
        self.assertEqual(orders, list(range(1, 31)))


# TESTING FILTER_DATA FUNCTION
"""
Note:
Defining test data
Calling filter_data function with prepared test data
Asserting on two Pandas DataFrame objects to be returned
Validating that the number of rows in each df meets expected values in the context of the input data -
filtered_by_comments is expected to have two rows as these entries have more than five words in the title.
filtered_by_points is expected to have one row as only one entry has five or fewer words.
Separately sorting the df by comments and points in descending order using sort_values method, which orders rows in
df based on the column values for comments / points.
Sorted dataframes are compared to the original dataframes in the test set-up
If sorted dataframes match the ones returned by filter_data, the assertions (assert_frame_equal) will pass and test
succeeds => filter_data is correctly sorting the data based on comments / points.
"""
# ---Test Expectations---
# Testing if outputs from filtered_data are pandas df
# Testing if length of df matches expected values
# Testing if data is sorted correctly by comments / points


class TestFilterData(unittest.TestCase):
    def setUp(self):
        self.data = [
            # Setting up test data with varying values for dict keys for later sorting
            {"order": 1, "title": "Short title", "points": "15 points", "comments": "3 comments"},

            {"order": 2, "title": "This is a long title with more than five words", "points": "20 points",
             "comments": "14 comments"},

            {"order": 3, "title": "This title also has more than five words", "points": "10 points",
             "comments": "8 comments"},
        ]

    @patch('pandas.DataFrame.to_csv', new_callable=MagicMock)
    def test_filter_data(self, mock_to_csv):
        filtered_by_comments_df, filtered_by_points_df = filter_data(self.data)

        # Assert on the function returning dataframes
        self.assertIsInstance(filtered_by_comments_df, pd.DataFrame)
        self.assertIsInstance(filtered_by_points_df, pd.DataFrame)

        # Assert on content of returned dataframes
        # 2 entries with more than 5 words in title
        self.assertEqual(len(filtered_by_comments_df), 2)
        # 1 entry with 5 or fewer words in title
        self.assertEqual(len(filtered_by_points_df), 1)

        # Validating filtering of filtered_by_comments is done correctly
        sorted_comments_df = filtered_by_comments_df.sort_values(by='comments', ascending=False)
        pd.testing.assert_frame_equal(filtered_by_comments_df, sorted_comments_df)

        # Validating filtering of filtered_by_points is done correctly
        sorted_points_df = filtered_by_points_df.sort_values(by='points', ascending=False)
        pd.testing.assert_frame_equal(filtered_by_points_df, sorted_points_df)

        # Assert to_csv has been called on df but not written to disk
        self.assertEqual(mock_to_csv.call_count, 3)


if __name__ == '__main__':
    unittest.main()

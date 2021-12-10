#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
import unittest

from data.yfinance_data_catcher import YFinanceDataCatcher


class YFinanceDataCatcherTest(unittest.TestCase):
    def test_catch_data(self):
        start_date = "2020-01-01"
        end_date = "2020-01-02"
        ETH_USD = "eth-usd"

        yfinance_data_catcher = YFinanceDataCatcher()
        data = yfinance_data_catcher.get_data(ETH_USD, start_date, end_date)
        self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)
        data.reset_index(inplace=True)
        self.assertEqual(str(data.iloc[0]["Date"]), "2020-01-01 00:00:00")
        self.assertEqual(str(data.iloc[1]["Date"]), "2020-01-02 00:00:00")

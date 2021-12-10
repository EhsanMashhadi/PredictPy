#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
import unittest
import pandas as pd

from data.data_statistic import DataStatistic


class DataTest(unittest.TestCase):
    def test_statistics(self):
        try:
            d = {'col1': [1, 2], 'col2': [3, 4]}
            df = pd.DataFrame(data=d)
            data_statistic = DataStatistic()
            data_statistic.show_data_statistic(df)
        except Exception:
            self.fail("Exception occurred: {}".format(Exception))

    def test_plot(self):
        try:
            d = {'col1': [1, 2, 2, 3, 1, 2, 3, 4], 'col2': [3, 4, 5, 6, 7, 8, 9, 5]}
            df = pd.DataFrame(data=d)
            data_statistic = DataStatistic()
            data_statistic.plot_data(df, "col1", "col2")
        except Exception:
            self.fail("Exception occurred: {}".format(Exception))

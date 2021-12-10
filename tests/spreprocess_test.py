#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
import unittest
import pandas as pd

from data.smodel_data_preprocessor import SeriesModelDataPreprocessor


class SeriesPreprocessTest(unittest.TestCase):
    def test_preprocess(self):
        d = {'Open': [1, 2], 'Date': [3, 4], 'End': [4, 6]}
        df = pd.DataFrame(data=d)
        smodel_preprocessor = SeriesModelDataPreprocessor()
        result = smodel_preprocessor.preprocess(df)
        self.assertEqual(len(result.columns), 2)
        self.assertTrue("ds" in result.columns)
        self.assertTrue("y" in result.columns)

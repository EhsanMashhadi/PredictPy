#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
import unittest

from model.time_series.time_series import TimeSeries
import pandas as pd


class TestTimeSeries(unittest.TestCase):
    def test_fit_bad_data(self):
        mock_data = {"col1": [1, 2], "col2": [3, 4]}
        time_series = TimeSeries(mock_data)
        try:
            time_series.fit_model()
        except ValueError:
            self.assertRaises(ValueError)

    def test_fit(self):
        mock_data = {"ds": ["2020-01-01 00:00:00", "2020-01-02 00:00:00"], "y": [3, 4]}
        data_frame = pd.DataFrame(mock_data)
        time_series = TimeSeries(data_frame)
        time_series.fit_model()

    def test_predict_without_train(self):
        mock_data = {"ds": ["2020-01-01 00:00:00", "2020-01-02 00:00:00"], "y": [3, 4]}
        data_frame = pd.DataFrame(mock_data)
        time_series = TimeSeries(data_frame)
        try:
            time_series.predict_future(5)
        except Exception:
            self.assertRaises(Exception)

    def test_predict(self):
        mock_data = {"ds": ["2020-01-01 00:00:00", "2020-01-02 00:00:00"], "y": [3, 4]}
        data_frame = pd.DataFrame(mock_data)
        time_series = TimeSeries(data_frame)
        time_series.fit_model()
        time_series.predict_future(5)

    def test_show_price_plot(self):
        try:
            mock_data = {"ds": ["2020-01-01 00:00:00", "2020-01-02 00:00:00"], "y": [3, 4]}
            data_frame = pd.DataFrame(mock_data)
            time_series = TimeSeries(data_frame)
            time_series.fit_model()
            time_series.predict_future(100)
            time_series.show_price_plot()
        except Exception:
            self.fail("Error has occurred")

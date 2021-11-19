#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from data.data_statistic import DataStatistic
from data.smodel_data_preprocessor import SeriesModelDataPreprocessor
from data.yfinance_data_catcher import YFinanceDataCatcher
from model.time_series.time_series import TimeSeries
from presenter.validator_wrapper import check_data, check_model


class SeriesModelPresenter(object):
    data = None
    model = None
    yahoo_finance_data_catcher = YFinanceDataCatcher()
    smodel_data_preprocessor = SeriesModelDataPreprocessor()
    data_statistic = DataStatistic()

    def get_data(self, symbol, start, end, force_update=False):
        if self.data is None or force_update is True:
            self.data = self.yahoo_finance_data_catcher.get_data(symbol, start, end)

    @check_data
    def show_data(self):
        self.data_statistic.show_data_statistic(self.data)

    @check_data
    def preprocess_data(self):
        self.data = self.smodel_data_preprocessor.preprocess(self.data)

    @check_data
    def plot_data(self):
        self.data_statistic.plot_data(self.data, "ds", "y")

    @check_data
    def create_model(self):
        self.model = TimeSeries(self.data)

    @check_data
    @check_model
    def train_model(self):
        self.model.fit_model()

    @check_data
    @check_model
    def predict_model(self, period=10):
        self.model.predict(period=period)

    @check_data
    @check_model
    def get_day_price(self, number=10):
        return self.model.get_day_price(number)

    def show_price_plot(self):
        self.model.show_price_plot()

    def show_price_components_plot(self):
        self.model.show_price_components_plot()

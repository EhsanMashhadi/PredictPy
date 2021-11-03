#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from data.data_statistic import DataStatistic
from data.tmodel_data_preprocessor import TransformerModelDataPreprocessor
from data.yfinance_data_catcher import YFinanceDataCatcher
from model.transformer.transformer_model import TransformerModel
from presenter.validator_wrapper import check_data


class TransformerPresenter(object):
    data = None
    eval_data = None
    yahoo_finance_data_catcher = YFinanceDataCatcher()
    transformer_model_data_preprocessor = TransformerModelDataPreprocessor()
    data_statistic = DataStatistic()
    model = TransformerModel()

    def get_data(self, symbol, start, end, force_update=False):
        if self.data is None or force_update is True:
            self.data = self.yahoo_finance_data_catcher.get_data(symbol, start, end)

    @check_data
    def preprocess_data(self):
        self.data = self.transformer_model_data_preprocessor.preprocess(self.data)

    @check_data
    def show_data(self):
        self.data_statistic.show_data_statistic(self.data)

    @check_data
    def plot_data(self, x_col_name, y_col_name):
        self.data_statistic.plot_data(self.data, x_col_name, y_col_name)

    def create_model(self):
        self.model.create_model()

    def model_summary(self):
        self.model.summary()

    def train(self):
        self.model.train(x_train=self.data["x_train"], y_train=self.data["y_train"], x_val=self.data["x_val"],
                         y_val=self.data["y_val"])

    def load(self):
        self.model.load()

    def evaluate(self):
        self.model.evaluate(x_train=self.data["x_train"], y_train=self.data["y_train"], x_val=self.data["x_val"],
                            y_val=self.data["y_val"], x_test=self.data["x_test"], y_test=self.data["y_test"])

    def show_result(self):
        pred_data = self.model.predict(self.data["x_train"], self.data["x_val"], self.data["x_test"])
        # concat = pd.concat([self.data["x_train"], self.data["y_train"]], axis=1)
        self.model.plot_results(original_data=self.data["x_test"], data_pred=pred_data[0],type="training")

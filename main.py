#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from datetime import datetime

from presenter.smodel_presenter import SeriesModelPresenter
from presenter.transformer_presenter import TransformerPresenter

import sys

today = datetime.today().strftime("%Y-%m-%d")


class Main(object):
    currency = None
    start_date = None

    # deciding between different currencies, methods, and specific start date
    def __init__(self, method, currency="btc-usd", start_date="2018-01-01"):
        self.currency = currency
        self.start_date = start_date
        if method == "rsm":
            self.run_series_model()
        elif method == "tes":
            self.train_evaluate_smodel()
        elif method == "ttm":
            self.train_transformer_model()
        elif method == "pt":
            self.predict_transformers()

    def run_series_model(self):
        smodel_presenter = SeriesModelPresenter()
        smodel_presenter.get_data(self.currency, self.start_date, today)
        smodel_presenter.show_data()
        smodel_presenter.preprocess_data()
        smodel_presenter.plot_data()
        smodel_presenter.create_model()
        smodel_presenter.train_model()
        smodel_presenter.predict_model(100)
        print("")
        price = smodel_presenter.get_day_price(10)
        print("The next {day} days price is : ".format(day=10))
        print(price)
        smodel_presenter.show_price_plot()
        smodel_presenter.show_price_components_plot()

    def train_evaluate_smodel(self):
        smodel_presenter = SeriesModelPresenter()
        smodel_presenter.get_data(self.currency, self.start_date, today)
        smodel_presenter.show_data()
        smodel_presenter.preprocess_data()
        smodel_presenter.plot_data()
        smodel_presenter.create_model()
        smodel_presenter.split_data()
        smodel_presenter.train()
        smodel_presenter.evaluate(12)

    def train_transformer_model(self):
        transformer_presenter = TransformerPresenter()
        transformer_presenter.get_data(self.currency, self.start_date, today)
        transformer_presenter.show_data()
        transformer_presenter.preprocess_data()
        transformer_presenter.plot_data("Date", "Close")
        transformer_presenter.split_data()
        transformer_presenter.create_model()
        transformer_presenter.model_summary()
        transformer_presenter.train()

    def predict_transformers(self):
        transformer_presenter = TransformerPresenter()
        transformer_presenter.get_data(self.currency, self.start_date, today)
        transformer_presenter.preprocess_data()
        transformer_presenter.split_data()
        transformer_presenter.load()
        transformer_presenter.evaluate()
        transformer_presenter.show_result()


if __name__ == '__main__':
    currency = "btc-usd"
    start_date = "2019-01-01"
    method = "rsm"
    # method ="tes"
    # method = "ttm"
    # method = "pt"
    main = Main(sys.argv[1], currency=sys.argv[2], start_date=sys.argv[3])

# sudo docker build -t tag1 .
# sudo docker run tag1 "ehsan"

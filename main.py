#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from datetime import datetime

from presenter.smodel_presenter import SeriesModelPresenter
from presenter.transformer_presenter import TransformerPresenter
import tensorflow as tf
ETH_USD = "eth-usd"
IBM_USD = "IBM"

class Main(object):

    def run_series_model(self):
        start_date = "2016-01-01"
        today = datetime.today().strftime("%Y-%m-%d")
        smodel_presenter = SeriesModelPresenter()
        smodel_presenter.get_data(ETH_USD, start_date, today)
        smodel_presenter.show_data()
        smodel_presenter.preprocess_data()
        smodel_presenter.plot_data()
        smodel_presenter.create_model()
        smodel_presenter.train_model()
        smodel_presenter.predict_model(100)

        # print("The next {day} days price is: ".format(day=20))
        price = smodel_presenter.get_day_price(10)
        print(price)
        smodel_presenter.show_price_plot()
        smodel_presenter.show_price_components_plot()

    def run_transformer_model(self):
        start_date = "1962-01-01"
        today = datetime.today().strftime("%Y-%m-%d")
        transformer_presenter = TransformerPresenter()
        transformer_presenter.get_data(IBM_USD, start_date, today)
        transformer_presenter.preprocess_data()
        # transformer_presenter.show_data()
        transformer_presenter.create_model()
        # transformer_presenter.model_summary()
        # transformer_presenter.plot_data("Date", "Close")
        # transformer_presenter.train()
        transformer_presenter.load()
        transformer_presenter.show_result()


if __name__ == '__main__':
    main = Main()
    main.run_transformer_model()

#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from datetime import datetime
from datetime import timedelta

from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly


class TimeSeries(object):
    data = None
    model = None
    forecast = None

    def __init__(self, data):
        self.data = data

    def fit_model(self):
        self.model = Prophet(seasonality_mode="multiplicative")
        self.model.fit(self.data)

    def predict(self, period):
        future = self.model.make_future_dataframe(periods=period)
        self.forecast = self.model.predict(future)
        print(self.forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

    def show_day_price(self, number_of_days):
        print("The next {day} days price is: ".format(day=number_of_days))
        intended_time = (datetime.today() + timedelta(days=number_of_days)).strftime("%Y-%m-%d")
        print(intended_time)
        output = self.forecast[self.forecast["ds"] == intended_time]["yhat"].item()
        print(output)

    def show_price_plot(self):
        plot_plotly(self.model, self.forecast).show()

    def show_price_components_plot(self):
        plot_components_plotly(self.model, self.forecast).show()

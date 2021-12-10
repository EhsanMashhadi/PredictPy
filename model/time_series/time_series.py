#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from datetime import datetime
from datetime import timedelta

from keras.losses import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from tensorflow.python.ops.metrics_impl import root_mean_squared_error


class TimeSeries(object):
    data = None
    model = None
    forecast = None

    def __init__(self, data):
        self.data = data

    def fit_model(self):
        self.model = Prophet(seasonality_mode="multiplicative")
        self.model.fit(self.data)

    def predict_future(self, period):
        future = self.model.make_future_dataframe(periods=period)
        self.forecast = self.model.predict(future)
        print(self.forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

    def predict_period(self, period):
        self.forecast = self.model.predict(period)
        return self.forecast

    def get_day_price(self, number_of_days):
        intended_time = (datetime.today() + timedelta(days=number_of_days)).replace(hour=0, minute=0,
                                                                                    second=0).strftime(
            "%Y-%m-%d %H:%M:%S")
        return self.forecast[self.forecast["ds"] == intended_time]["yhat"].item()

    def show_price_plot(self):
        plot_plotly(self.model, self.forecast).show()

    def show_price_components_plot(self):
        plot_components_plotly(self.model, self.forecast).show()

    def evaluate_model(self, y_true, y_pred):
        mae = mean_absolute_error(y_true, y_pred)
        mse = mean_squared_error(y_true, y_pred)
        mape = mean_absolute_percentage_error(y_true, y_pred)
        print('MAE: %.3f' % mae)
        print('MSE: %.3f' % mse)
        print('MAPE: %.3f' % mape)
        return mae

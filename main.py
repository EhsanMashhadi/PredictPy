#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from datetime import datetime

from data.data_catcher import DataCatcher
from model.time_series import TimeSeries


class Main(object):

    def get_data(self):
        data_catcher = DataCatcher()
        start_date = "2016-01-01"
        today = datetime.today().strftime("%Y-%m-%d")
        data = data_catcher.get_data(start_date, today)
        # data_catcher.show_data(data)
        time_series = TimeSeries(data)
        time_series.fit_model()
        time_series.predict(period=365)
        time_series.show_day_price(1)
        time_series.show_price_plot()
        time_series.show_price_components_plot()


if __name__ == '__main__':
    main = Main()
    main.get_data()

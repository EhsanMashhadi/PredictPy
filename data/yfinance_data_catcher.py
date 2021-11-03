#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from data.data_catcher import DataCatcher
import yfinance as yf


class YFinanceDataCatcher(DataCatcher):
    def get_data(self, symbol, start, end):
        data = yf.download(symbol, start, end)
        return data




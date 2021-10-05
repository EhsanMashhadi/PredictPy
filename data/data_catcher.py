#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
import plotly.graph_objects as go
import yfinance as yf


class DataCatcher(object):

    def get_data(self, start, end):
        eth_usd = yf.download('ETH-USD', start, end)

        print("\n")
        print("HEAD:")
        print(eth_usd.head())

        print("\n")
        print("Tail")
        print(eth_usd.tail())

        print("\n")
        print("Data Info:")
        print(eth_usd.info())

        print("\n")
        print("Is Null?")
        print(eth_usd.isnull().sum())

        print(eth_usd.columns)

        eth_usd.reset_index(inplace=True)
        eth_usd = eth_usd[["Date", "Open"]]

        eth_usd.columns = ["ds", "y"]
        print(eth_usd.tail())
        return eth_usd

    def show_data(self, data):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data["ds"], y=data["y"]))
        fig.update_layout(title="ETH/USD")
        fig.show()

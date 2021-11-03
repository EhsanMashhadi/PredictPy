#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.

import plotly.graph_objects as go


class DataStatistic(object):
    def show_data_statistic(self, data):
        print("\n")
        print("HEAD:")
        print(data.head())

        print("\n")
        print("Tail")
        print(data.tail())

        print("\n")
        print("Data Info:")
        print(data.info())

        print("\n")
        print("Is Null?")
        print(data.isnull().sum())

    def plot_data(self, data, x_col_name, y_col_name):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data[x_col_name], y=data[y_col_name]))
        fig.update_layout(title="{x_col_name} / {y_col_name}".format(x_col_name=x_col_name, y_col_name=y_col_name))
        fig.show()

#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from data.data_preprocessor import DataPreprocessor


# preprocessor class to do data preprocessing for transformer model

class TransformerModelDataPreprocessor(DataPreprocessor):
    seq_len = 128

    def preprocess(self, data):
        data = self.reset_index(data)
        return data

    def split_data(self, data):
        data = self.percentage_change(data)
        self.drop_na_values(data)
        x_col = ['Open', 'High', 'Low', 'Close']
        y_col = ['Volume']
        data_train = data[0:int(len(data) * 0.8)]
        data_val = data[int(len(data) * 0.8): int(len(data) * 0.9)]
        data_test = data[int(len(data) * 0.9):]

        data_train_x = self.min_max(data_train[x_col])
        data_train_y = self.min_max(data_train[y_col])
        concat = pd.concat([data_train_x, data_train_y], axis=1)
        x_train, y_train = self.create_chunks(concat.values)

        data_val_x = self.min_max(data_val[x_col])
        data_val_y = self.min_max(data_val[y_col])
        concat = pd.concat([data_val_x, data_val_y], axis=1)
        x_val, y_val = self.create_chunks(concat.values)

        data_test_x = self.min_max(data_test[x_col])
        data_test_y = self.min_max(data_test[y_col])
        concat = pd.concat([data_test_x, data_test_y], axis=1)
        x_test, y_test = self.create_chunks(concat.values)

        print("Shape")
        print(x_train.shape, y_train.shape)
        print(x_val.shape, y_val.shape)

        return {"x_train": x_train, "x_val": x_val, "x_test": x_test, "y_train": y_train, "y_val": y_val,
                "y_test": y_test}

    def percentage_change(self, data):
        data['Open'] = data['Open'].pct_change()
        data['High'] = data['High'].pct_change()
        data['Low'] = data['Low'].pct_change()
        data['Close'] = data['Close'].pct_change()
        data['Volume'] = data['Volume'].pct_change()
        return data

    def drop_na_values(self, data):
        # Replace inf -inf with NaN
        data.replace([np.inf, -np.inf], np.nan, inplace=True)
        # Drop all rows with NaN values
        data.dropna(how='any', axis=0, inplace=True)

    def reset_index(self, data):
        data.reset_index(inplace=True)
        return data

    def min_max(self, data):
        trans = MinMaxScaler()
        data = pd.DataFrame(trans.fit_transform(data), columns=data.columns)
        return data

    def create_chunks(self, data):
        x_data, y_data = [], []
        for i in range(self.seq_len, len(data)):
            x_data.append(data[i - self.seq_len:i])
            y_data.append(data[:, 3][i])
        x_data, y_data = np.array(x_data), np.array(y_data)
        return x_data, y_data

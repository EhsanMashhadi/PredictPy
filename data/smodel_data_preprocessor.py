#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from data.data_preprocessor import DataPreprocessor


# preprocessor class to do data preprocessing for prophet series model

class SeriesModelDataPreprocessor(DataPreprocessor):

    def preprocess(self, data):
        return self.reset_index(data)

    def reset_index(self, data):
        data.reset_index(inplace=True)
        data = data[["Date", "Open"]]
        data.columns = ["ds", "y"]
        return data

    def split_data(self, data, test_months=12):
        train = data.drop(data.index[-test_months:])
        test = data.tail(test_months)
        return {"train": train, "test": test}

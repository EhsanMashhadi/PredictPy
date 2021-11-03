#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from abc import ABC, abstractmethod


class DataPreprocessor(ABC):

    def preprocess(self, data):
        pass

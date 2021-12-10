#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
from abc import ABC, abstractmethod


# abstract class for different data catchers

class DataCatcher(ABC):

    @abstractmethod
    def get_data(self, symbol, start, end):
        pass

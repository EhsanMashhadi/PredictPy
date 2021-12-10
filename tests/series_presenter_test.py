#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
import unittest
from unittest.mock import MagicMock

from presenter.smodel_presenter import SeriesModelPresenter


class TestTimeSeriesPresenter(unittest.TestCase):
    def test_p1(self):
        spresenter = SeriesModelPresenter()
        spresenter.get_data = MagicMock(return_value=1)
        spresenter.get_data("ETH", "re", "re")
        spresenter.get_data.assert_called()
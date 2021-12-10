#  Copyright Ehsan Mashhadi, 2021 Licensed under MIT License.
#  See the LICENSE.txt for more information.
import unittest

from presenter.validator_wrapper import check_data, check_model


class TestValidatorWrapper(unittest.TestCase):
    data = None
    model = None

    def test_check_data_none(self):
        self.data = None
        try:
            self.check_data()
        except Exception:
            self.assertRaises(Exception)

    def test_check_model_none(self):
        self.model = None
        try:
            self.check_model()
        except Exception:
            self.assertRaises(Exception)

    def test_check_data_not_none(self):
        self.data = "mock data"
        try:
            self.check_data()
        except Exception:
            self.fail("Exception occurred")

    def test_check_model_not_none(self):
        self.model = "mock model"
        try:
            self.check_model()
        except Exception:
            self.fail("Exception occurred")

    @check_data
    def check_data(self):
        pass

    @check_model
    def check_model(self):
        pass

from unittest import TestCase
from main import BoundedValue

class TestBoundedValue(TestCase):

    def test_init(self):
        # arrange
        expected_min = 10
        expected_max = 20

        # act
        value = BoundedValue(expected_min, expected_max)
        actual_min = value.get_min()
        actual_max = value.get_max()
        actual_value = value.get_value()

        # assert
        self.assertEqual(expected_min, actual_min)
        self.assertEqual(expected_max, actual_max)
        self.assertTrue(expected_min <= actual_value <= expected_max)

    def test_set_value_fails(self):
        # arrange
        expected_min = 10
        expected_max = 20
        value = BoundedValue(expected_min, expected_max)
        expected_error_message = "Invalid value"

        # act
        actual_error_message = ""
        try:
            value.set_value(5)
        except ValueError as e:
            actual_error_message = str(e)

        # assert
        self.assertEqual(expected_error_message, actual_error_message)

    def test_set_value_works(self):
        # arrange
        expected_min = 10
        expected_max = 20
        expected_value = 15
        value = BoundedValue(expected_min, expected_max)

        # act
        value.set_value(expected_value)
        actual_value = value.get_value()

        # assert
        self.assertEqual(expected_value, actual_value)

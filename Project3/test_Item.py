from unittest import TestCase
from item import Item

class TestItem(TestCase):

    def test_init(self):
        # arrange
        expected_name = 'bananas'
        expected_unit_price = .3
        expected_quantity = 7
        expected_total_price = 2.1
        expected_string = '7 bananas @ $0.3/each - $2.1'

        # act
        bananas = Item(expected_name, expected_quantity, expected_unit_price)
        actual_name = bananas.get_name()
        actual_unit_price = bananas.get_unit_price()
        actual_quantity = bananas.get_quantity()
        actual_total_price = bananas.get_total_price()
        actual_string = str(bananas)

        # assert
        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_unit_price, actual_unit_price)
        self.assertEqual(expected_quantity, actual_quantity)
        self.assertEqual(expected_total_price, actual_total_price)
        self.assertEqual(expected_string, actual_string)

    def test_set_unit_price_negative(self):
        # arrange
        item = Item("")
        expected_unit_price = 0

        # act
        item.set_unit_price(-1)
        actual_unit_price = item.get_unit_price()

        # assert
        self.assertEqual(expected_unit_price, actual_unit_price)

    def test_set_unit_price(self):
        # arrange
        item = Item("")
        expected_unit_price = 7

        # act
        item.set_unit_price(expected_unit_price)
        actual_unit_price = item.get_unit_price()

        # assert
        self.assertEqual(expected_unit_price, actual_unit_price)

    def test_set_quantity_negative(self):
        # arrange
        item = Item("")
        expected_quantity = 0

        # act
        item.set_quantity(-1)
        actual_quantity = item.get_quantity()

        # assert
        self.assertEqual(expected_quantity, actual_quantity)

    def test_set_quantity(self):
        # arrange
        item = Item("")
        expected_quantity = 7

        # act
        item.set_quantity(expected_quantity)
        actual_quantity = item.get_quantity()

        # assert
        self.assertEqual(expected_quantity, actual_quantity)

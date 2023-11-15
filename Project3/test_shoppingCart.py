from unittest import TestCase
from shoppingCart import ShoppingCart
from item import Item

class TestShoppingCart(TestCase):
    def test_receipt(self):
        # arrange
        expected_receipt = '7 bananas @ $0.3/each - $2.1\n'
        expected_receipt += '1 peanut butter @ $2.99/each - $2.99\n'
        expected_receipt += "Grand Total: $5.09"
        cart = ShoppingCart()
        bananas = Item('bananas', 7, .3)
        peanut_butter = Item("peanut butter", 1, 2.99)
        cart.add_item(bananas)
        cart.add_item(peanut_butter)

        # act
        actual_receipt = cart.receipt()

        # assert
        self.assertEqual(expected_receipt, actual_receipt)
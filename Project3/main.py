from shoppingCart import ShoppingCart
from item import Item

choice = ''
cart = ShoppingCart()

while choice != 'q':
    choice = input("Do you want (a)dd an item, print (r)eceipt, or (q)uit")

    if choice == "a":
        item_name = input("Enter the item name")
        quantity = int(input("Enter the quantity"))
        unit_price = float(input("Enter the unit price"))
        cart.add_item(Item(item_name, quantity, unit_price))
    elif choice == "r":
        print(cart.receipt())
        
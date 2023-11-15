class Item:

    def __init__(self, name, quantity = 0, unit_price = 0):
        self._name = name
        self.set_quantity(quantity)
        self.set_unit_price(unit_price)
    def get_name(self):
        return self._name

    def get_unit_price(self):
        return self._unit_price

    def get_quantity(self):
        return self._quantity

    def get_total_price(self):
        return self._quantity * self._unit_price

    def set_unit_price(self, unit_price):
        if unit_price > 0:
            self._unit_price = unit_price
        else:
            self._unit_price = 0

    def set_quantity(self, quantity):
        if quantity > 0:
            self._quantity = quantity
        else:
            self._quantity = 0

    def __str__(self):
        return f'{self._quantity} {self._name} @ ${self._unit_price}/each - ${self.get_total_price()}'
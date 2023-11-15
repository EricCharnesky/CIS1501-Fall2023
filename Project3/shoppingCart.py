
class ShoppingCart:

    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def receipt(self):
        result = ""
        total = 0
        for item in self._items:
            result += str(item) + "\n"
            total += item.get_total_price()
        result += f"Grand Total: ${total}"

        return result

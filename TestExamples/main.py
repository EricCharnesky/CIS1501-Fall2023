import random


class BoundedValue:

    def __init__(self, min, max):
        if max < min:
            raise ValueError("Invalid min and max")
        self._min = min
        self._max = max
        self._value = random.randint(min, max)

    def get_min(self):
        return self._min

    def get_max(self):
        return self._max

    def get_value(self):
        return self._value

    def set_value(self, value):
        if value < self._min or value > self._max:
            raise ValueError("Invalid value")
        self._value = value


if __name__ == "__main__":
    value = BoundedValue(10,20)
    print(value.get_min())
    print(value.get_max())

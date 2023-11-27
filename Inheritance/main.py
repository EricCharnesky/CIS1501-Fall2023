class Polygon:

    def __init__(self, number_of_sides):
        self._side_lengths = []
        for side in range(number_of_sides):
            self._side_lengths[side] = 0

    def set_side_length(self, side_index, length):
        self._side_lengths[side_index] = length

    def get_perimeter(self):
        return sum(self._side_lengths)

    def get_side_length(self, side_index):
        return self._side_lengths[side_index]


class Rectangle(Polygon):

    def __init__(self, length, width):
        super().__init__(4)
        self.set_length(length)
        self.set_width(width)

    def get_length(self):
        return self.get_side_length(0)

    def get_width(self):
        return self.get_side_length(1)

    def set_length(self, length):
        if length < 0:
            length = 0
        self.set_side_length(0, length)
        self.set_side_length(2, length)

    def set_width(self, width):
        if width < 0:
            width = 0
        self.set_side_length(1, width)
        self.set_side_length(3, width)

    def get_area(self):
        return self.get_length() * self.get_width()


class Square(Rectangle):

    def __init__(self, size):
        super().__init__(size, size)

    # ensures it stays a square
    def set_length(self, length):
        super().set_width(length)
        super().set_length(length)

    def set_width(self, width):
        super().set_width(width)
        super().set_length(width)


small_square = Rectangle(10, 10)
small_square.set_width(20) # oops - no longer a square

actual_square = Square(10)

actual_square.get_area()


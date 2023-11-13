import random


class ElectricCar:

    def __init__(self, make, model, color, max_kilowatt_hours_in_battery, kilometers_per_kilowatt_hour):
        self._make = make
        self._model = model
        self._color = color
        self._odometer_in_kilometers = 0
        self._max_kilowatt_hours_in_battery = max_kilowatt_hours_in_battery
        self._current_kilowatt_hours_in_battery = 0
        self._kilometers_per_kilowatt_hour = kilometers_per_kilowatt_hour

    def charge(self, kilowatt_hours_to_charge):
        self._current_kilowatt_hours_in_battery += kilowatt_hours_to_charge
        if self._current_kilowatt_hours_in_battery > self._max_kilowatt_hours_in_battery:
            self._current_kilowatt_hours_in_battery = self._max_kilowatt_hours_in_battery

    def drive(self, number_of_kilometers):
        if 0 < number_of_kilometers <= self._current_kilowatt_hours_in_battery * self._kilometers_per_kilowatt_hour:
            self._current_kilowatt_hours_in_battery -= number_of_kilometers / self._kilometers_per_kilowatt_hour
            self._odometer_in_kilometers += number_of_kilometers
        else:
            raise ValueError("Not enough charge to drive that far!")

    def get_max_kilowatt_hours_in_battery(self):
        return self._max_kilowatt_hours_in_battery

    def get_current_kilowatt_hours_in_battery(self):
        return self._current_kilowatt_hours_in_battery

    def get_kilometers_per_kilowatt_hour(self):
        return self._kilometers_per_kilowatt_hour

    def get_odometer(self):
        return self._odometer_in_kilometers

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color





# encapsulated all the details of chair into the chair class
# can protect the chair attributes to be within valid ranges
# best practice is to have all private attributes with public functions to set/get as appropriate
class Chair:

    def __init__(self):
        self._color = "black"
        self.has_wheels = True

        # using an underscore denotes the attribute is 'private'
        self._height_of_seat_in_centimeters = 90
        self.minimum_height_in_centimeters = 45
        self.maximum_height_in_centimeters = 125

    def __str__(self):
        return (f"{self._color} chair with the seat set to {self._height_of_seat_in_centimeters} "
                f"cm with { 'wheels' if self.has_wheels else 'no wheels'}") # FIX ME

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_height_of_seat_in_centimeters(self):
        return self._height_of_seat_in_centimeters

    def change_height(self, new_height_in_centimeters):
        self.height_of_seat_in_centimeters = new_height_in_centimeters

        # sanity check of the argument
        if self.height_of_seat_in_centimeters < self.minimum_height_in_centimeters:
            self.height_of_seat_in_centimeters = self.minimum_height_in_centimeters
        elif self.height_of_seat_in_centimeters > self.maximum_height_in_centimeters:
            self.height_of_seat_in_centimeters = self.maximum_height_in_centimeters



def print_car(car):
    print("Make", car.get_make())
    print("Model", car.get_model())
    print("Color", car.get_color())
    print("Odometer", car.get_odometer())
    print("Current Kilowatt Hours", car.get_current_kilowatt_hours_in_battery())


# prevents this code from running, unless this module was the file ran, not imported
if __name__ == '__main__':

    erics_chair = Chair() # calls the __init__ functions

    print(erics_chair)
    erics_chair.has_wheels = False
    print(erics_chair)

    erics_chair_color = "blue"
    erics_chair_has_wheels = True

    # changes the value of the attribute
    erics_chair.color = "blue"

    jebs_chair = Chair()
    jebs_chair.has_wheels = False

    print("Eric's Chair:")
    print(erics_chair.get_height_of_seat_in_centimeters())
    print(erics_chair.has_wheels)

    print("Jebs's Chair:")
    print(jebs_chair.get_height_of_seat_in_centimeters())
    print(jebs_chair.has_wheels)

    erics_chair.change_height(500)
    #print(erics_chair._height_of_seat_in_centimeters)
    erics_chair._height_of_seat_in_centimeters = 500
    #print(erics_chair._height_of_seat_in_centimeters)



    # work with functions absrtactly - we don't know the details
    print(random.randint(1, 100))

    erics_car = ElectricCar("Chevy", "Bolt", "Grey", 133, 5)

    print(erics_car.get_make())

    #jasmines_van = Car("Ford", "Transit", "Blue Jean")

    #print(jasmines_van.get_make())
    erics_car.charge(150)
    print_car(erics_car)
    #print_car(jasmines_van)

    erics_car.drive(47)

    print_car(erics_car)
    #print_car(jasmines_van)

    while True:
        try:
            erics_car.drive(int(input("How many KM do you want to drive?")))
            erics_car.drive(int(input("How many KM do you want to drive?")))
            erics_car.drive(int(input("How many KM do you want to drive?")))

            break
        except Exception as e:
            print(e)



    some_list = []
    print(some_list[1])


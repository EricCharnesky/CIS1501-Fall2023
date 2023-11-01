from unittest import TestCase
import main


class TestElectricCar(TestCase):
    def test_init(self):
        # arrange - setup all the variables we need to test
        expected_make = "Chevy"
        expected_model = "Bolt"
        expected_color = "Grey"
        expected_odometer_in_kilometers = 0
        expected_max_kilowatt_hours_in_battery = 250
        expected_current_kilowatt_hours_in_battery = 0
        expected_kilometers_per_kilowatt_hour = 5

        # act - call the code we are testing
        car = main.ElectricCar(expected_make, expected_model, expected_color, expected_max_kilowatt_hours_in_battery, expected_kilometers_per_kilowatt_hour)
        actual_make = car.get_make()
        actual_model = car.get_model()
        actual_color = car.get_color()
        actual_odometer_in_kilometers = car.get_odometer()
        actual_max_kilowatt_hours_in_battery = car.get_max_kilowatt_hours_in_battery()
        actual_current_kilowatt_hours_in_battery = car.get_current_kilowatt_hours_in_battery()
        actual_kilometers_per_kilowatt_hour = car.get_kilometers_per_kilowatt_hour()

        # assert - did we get what we expected
        self.assertEqual(expected_make, actual_make)
        self.assertEqual(expected_model, actual_model)
        self.assertEqual(expected_color, actual_color)
        self.assertEqual(expected_odometer_in_kilometers, actual_odometer_in_kilometers)
        self.assertEqual(expected_max_kilowatt_hours_in_battery, actual_max_kilowatt_hours_in_battery)
        self.assertEqual(expected_current_kilowatt_hours_in_battery, actual_current_kilowatt_hours_in_battery)
        self.assertEqual(expected_kilometers_per_kilowatt_hour, actual_kilometers_per_kilowatt_hour)

    def test_charge(self):
        # arrange
        expected_current_kilowatt_hours_in_battery = 250
        car = main.ElectricCar("", "","", expected_current_kilowatt_hours_in_battery, 0)

        # act
        car.charge(expected_current_kilowatt_hours_in_battery + 1)
        actual_current_kilowatt_hours_in_battery = car.get_current_kilowatt_hours_in_battery()

        # assert
        self.assertEqual(expected_current_kilowatt_hours_in_battery, actual_current_kilowatt_hours_in_battery)

    def test_drive_successful(self):
        # arrange
        expected_drive_result = True
        expected_odometer_in_kilometers = 5
        expected_current_kilowatt_hours_in_battery = 9
        car = main.ElectricCar("", "", "", 10, 5)
        car.charge(10)

        # act
        actual_drive_result = car.drive(expected_odometer_in_kilometers)
        actual_odometer_in_kilometers = car.get_odometer()
        actual_current_kilowatt_hours_in_battery = car.get_current_kilowatt_hours_in_battery()

        # assert
        self.assertEqual(expected_drive_result, actual_drive_result)
        self.assertEqual(expected_odometer_in_kilometers, actual_odometer_in_kilometers)
        self.assertEqual(expected_current_kilowatt_hours_in_battery, actual_current_kilowatt_hours_in_battery)

    def test_drive_unsuccessful(self):
        # arrange
        expected_drive_result = False
        expected_odometer_in_kilometers = 0
        expected_current_kilowatt_hours_in_battery = 0
        car = main.ElectricCar("", "", "", 0, 0)

        # act
        actual_drive_result = car.drive(1)
        actual_odometer_in_kilometers = car.get_odometer()
        actual_current_kilowatt_hours_in_battery = car.get_current_kilowatt_hours_in_battery()

        # assert
        self.assertEqual(expected_drive_result, actual_drive_result)
        self.assertEqual(expected_odometer_in_kilometers, actual_odometer_in_kilometers)
        self.assertEqual(expected_current_kilowatt_hours_in_battery, actual_current_kilowatt_hours_in_battery)

    def test_set_color(self):
        # arrange
        expected_color = "Blue"
        car = main.ElectricCar("", "", "black", 0, 0)

        # act
        car.set_color(expected_color)
        actual_color = car.get_color()

        # assert
        self.assertEqual(expected_color, actual_color)

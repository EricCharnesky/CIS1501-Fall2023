import math

name = input("Please enter your name")

expected_guests = int(input(name + ", how many guests do you expect?"))

food = input(name + ", what do you want to serve? pizza, drinks, or ice cream").lower()

if food == "pizza":
    slices_per_guest = float(input(name + ", how many slices does the average guest eat?"))
    slices_per_pizza = int(input(name + ", how many slices come per pizza"))
    cost_per_pizza = float(input(name + ", how much does a pizza cost?"))

    number_of_pizzas = math.ceil(slices_per_guest * expected_guests / slices_per_pizza)

    print(name + ", you need to buy", number_of_pizzas, "pizzas, for a cost of $", number_of_pizzas * cost_per_pizza )
elif food == "drinks":
    print('drinks')
elif food == "ice cream":
    print('ice cream')
else:
    print("I can't help with", food)
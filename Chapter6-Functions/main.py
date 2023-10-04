import random


def happy_monday():
    print("Happy Monday!")
    print("We're going to need more coffee!")


def happy_day(day):
    print("Happy", day)
    print("We're going to need some espresso")


def get_users_throw():
    users_throw = ""
    options = ("rock", "paper", "scissors")
    while users_throw not in options:
        users_throw = input("Enter rock, paper, or scissors").lower()
        # users_throw = users_throw.lower()

    return users_throw


def get_computers_throw():
    random_number = random.randint(1, 3)

    if random_number == 1:
        computers_throw = "rock"
        # return "rock"
    elif random_number == 2:
        computers_throw = "paper"
        # return "paper"
    else:
        computers_throw = "scissors"
        # return "scissors"

    return computers_throw

    print("function will never get here")


def display_results(users_throw, computers_throw):
    # letter = users_throw[0]
    # crashes if we don't give a string ( mostly )

    if users_throw == computers_throw:
        print("Draw")
    elif (users_throw == "rock" and computers_throw == "scissors") \
        or (users_throw == "paper" and computers_throw == "rock") \
        or (users_throw == "scissors" and computers_throw == "paper"):
        print("Player wins!")
    else:
        print("Player loses!")


def if_you_are_happy_and_you_know_it(action, verse):
    if verse < 3:
        print("If you're happy and you know it", action)
    else:
        print("If you're happy and you know it and you really want to show it", action)


# TODO - get weather data from online
def get_weather():
    return 70, "sunny"






def print_greeting(name, greeting):
    """calls the greeting function passed, then prints name"""
    greeting()
    print(name)


def tired_greeting():
    print("Hi, I'm tired")


def coffee_induced_hyper_greeting():
    print("Hi there, I'm having a great day, how are you, did you get any coffee?")

value = 0
value_to_add = 10

def add_ten():
    value = value_to_add
    print(value)
    return value

def upper_case_name(name):
    name = name.upper()
    print(name)
    return name

first_name = "eric"
print(first_name)
upper_case_name(first_name)
first_name = upper_case_name(first_name) # will change where first_name points to a string in memory
print(first_name)

def add_to_list(some_list):
    some_list.append(10)

def reassign_list(some_list):
    some_list = [10, 20, 30]
    print(some_list)


my_list = [1, 2, 3]
print(my_list)
add_to_list(my_list)
print(my_list)
reassign_list(my_list)
print(my_list)


def int(value):
    return 10

def randint(first, second):
    return 10

print(random.randint)

your_number = int(input("Enter your number"))
print(your_number)


another_value = add_ten()
more_values = add_ten()
value = add_ten()
print(add_ten())
print(value)


def citation_generator(author, title, publisher, year):
    print(f"{author}, {title}, {publisher}, {year}")

citation_generator("Bailey Miller", "Programming in Python 3", "Zyante Inc", "2023")

# optional keyword arguments
citation_generator(title="Programming in Python 3", year="2023", publisher="Zyante", author="Bailey")

def print_date(year = '2023', month = '10', day = '04'):
    print(f'{year}-{month}-{day}')


print_date('2023', '10', '04')

print_date("2022", "4")

print_date("2020")

print_date(day="05", month="04")

random.randrange(10)
range(10)
range(1, 10)
range(1, 10, 2)

def print_triangle(size, character="*"):
    for row in range(1, size+1):
        print(row * character)

print_triangle(10)

print_triangle(10, "&")

print_triangle(5, "#")

tired_greeting()
coffee_induced_hyper_greeting()
print_greeting("eric", tired_greeting) # passes the function as an argument
print_greeting("eric", coffee_induced_hyper_greeting)

random.randint(1, 10)


def get_grade_details():
    return "eric", "A+"


name, grade = get_grade_details()

result_tuple = get_grade_details()

my_name = result_tuple[0]
my_grade = result_tuple[1]

print(name, grade)
print(my_name, my_grade)


day = "monday"
print(day)

# have to declare variables AND functions before you use them
# print(another_day)
# another_day = "Tuesday"

print("happy monday!")

number = random.randint(1, 20)

happy_monday()
happy_day("monday")

print("Your powerball numbers are ")
for number in range(5):
    print(random.randint(1, 69), end=" ")
print("Powerball number: ", random.randint(1,26))
print()

play_again = 'y'

while play_again.lower() == "y":

    # more verbose way
    #users_throw = get_users_throw()
    #computers_throw = get_computers_throw()
    #display_results(users_throw, computers_throw)

    # shorter way
    display_results(get_users_throw(), get_computers_throw())

    play_again = input("Do you want to play again? y/n")

for verse in range(1, 4):
    if_you_are_happy_and_you_know_it("clap your hands", verse)

# you can give weird values to functions
display_results(1, 2)

temp, description = get_weather()
if temp > 65:
    if description == "sunny":
        print("put on sun screen")
    print("wear a t-shirt")
else:
    print("You need a jacket")


def get_item(items):
    pass # placeholder


items = []
more_items_to_buy = "y"

while more_items_to_buy == "y":
    get_item(items)
    more_items_to_buy = input("Do you have more items to buy? y/n")




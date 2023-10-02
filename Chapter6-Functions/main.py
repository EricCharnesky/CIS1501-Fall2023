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


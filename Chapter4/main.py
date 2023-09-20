import random

# boolean expression - something that is true or false
number_to_guess = random.randint(1, 100)

guess = int(input("Guess a number 1-100"))

# logical operator AND OR NOT

# AND - BOTH must be true
# true and true == true
# true and false == false
# false and true == false
# false and false == false

# OR - ONE must be true
# true or true == true
# ture or false == true
# false or ture == true
# false or false == false


if guess >= 1 and guess <= 100:
    print("valid guess")

# combine ranges in python
if 1 <= guess <= 100:
    print("valid guess")

if guess < 1 or guess > 100:
    print("invaid guess, please guess again")

if guess == number_to_guess:
    print("You got it!")
elif guess < number_to_guess:
    print("too low")
else:
    print("too high")

score = int(input("Please enter your score 0-100"))

# if elif chains are mutually exclusive
# - one and only one will run
if score >= 94:
    print("A")
elif score >= 90:
    print("A-")
elif score >= 87:
    print("B+")
    #....
    #....
else:
    print("F")


if 94 <= score <= 100:
    print("A")
# no elif because we have ranges
if 90 <= score < 94:
    print("A-")
if 87 <= score < 90:
    print("B+")


house_cost = int(input("Enter the cost of the house"))
down_payment = int(input("Enter the down payment"))
credit_score = int(input("Enter your credit score"))

if down_payment / house_cost >= .2:
    print("You get a mortgage!")
elif down_payment / house_cost >= .1 and credit_score > 700:
    print("You get a mortgage!")
else:
    print("No mortgage!")



if ( down_payment / house_cost >= .2 ) or \
    ( down_payment / house_cost >= .1 and credit_score > 700 ):
    print("You get a mortgage!")
else:
    print("No mortgage!")


food = input("What do you want to serve? pizza, drinks, or ice cream")

if food != "pizza" and food != "drinks" and food != "ice cream":
    print("invalid choice!")
    food = input("What do you want to serve? pizza, drinks, or ice cream")

party_options = ['pizza', 'drinks', 'ice cream']

if food not in party_options:
    print("invalid choice!")
    food = input("What do you want to serve? pizza, drinks, or ice cream")


lotto_ticket = []

number = int(input("Enter a number 1 - 69"))
lotto_ticket.append(number)

number = int(input("Enter a number 1 - 69"))
if number not in lotto_ticket:
    lotto_ticket.append(number)
else:
    print("You already used that number")

number = int(input("Enter a number 1 - 69"))
if number not in lotto_ticket:
    lotto_ticket.append(number)
else:
    print("You already used that number")

number = int(input("Enter a number 1 - 69"))
if number not in lotto_ticket:
    lotto_ticket.append(number)
else:
    print("You already used that number")

number = int(input("Enter a number 1 - 69"))
if number not in lotto_ticket:
    lotto_ticket.append(number)
else:
    print("You already used that number")

number = int(input("Enter a number 1 - 69"))
if number not in lotto_ticket:
    lotto_ticket.append(number)
else:
    print("You already used that number")

print(lotto_ticket)
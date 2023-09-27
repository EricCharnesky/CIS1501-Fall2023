import random

max_number = int(input("How high of a number do you want to guess?"))

number_to_guess = random.randint(1, max_number)

guess = int(input(f"Guess a number 1 - {max_number}: "))

# validation loop
while guess < 1 or guess > max_number:
    guess = int(input(f"Guess a number 1 - {max_number}: "))

number_of_guesses = 1
# runs as long as the expression is true
while guess != number_to_guess and number_of_guesses <= 5:

    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")

    # ends the loop - but in a confusing spot
    if number_of_guesses == 5:
        break

    guess = int(input(f"Guess a number 1 - {max_number}: "))
    number_of_guesses += 1



print(f"You guessed it in {number_of_guesses} guesses!")


choice = input("Rock, Paper, or Scissors?").lower()
valid_options = ('rock', 'paper', 'scissors')

#while choice != "Rock" and choice != "Paper" and choice != "Scissors":
while choice not in valid_options:
    choice = input("Rock, Paper, or Scissors?").lower()

computer_throw = ""
computer_choice = random.randint(1, 3)
if computer_choice == 1:
    computer_throw = "rock"
elif computer_choice == 2:
    computer_throw = "paper"
else:
    computer_throw = "scissors"

# shortcut
computer_throw = random.choice(valid_options)


highest_number = 0
number = int(input("Enter a number or 0 to stop"))
# sentinel value
while number != 0:
    if number > highest_number:
        highest_number = number
    number = int(input("Enter a number or 0 to stop"))
print(f"Highest number is {highest_number}")


total = 0
receipt_count = 0
# throw away value - makes sure the loop runs once
receipt = 1

while receipt != 0:
    receipt = float(input("Enter a receipt or 0 to stop"))
    total += receipt
    if receipt != 0:
        receipt_count += 1

print(f"total receipts {total} - average {total / receipt_count}")

# for loop - for every item in a collection

for letter in "Eric":
    print(letter.upper(), end="")
print() # blank line

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# for variable_name_for_single_item in collection
for color in colors:
    print(color)

total_points = 0
game = 1
while game <= 9:
    score = int(input(f"Enter the score for game #{game}"))
    total_points += score
    game += 1
print(f"Total season points: {total_points}")


total_points = 0
# range does not include the max
for game in range(1, 10):
    score = int(input(f"Enter the score for game #{game}"))
    total_points += score

# use underscore as a throwaway value
# range( start is assumed 0 )
# range(0, 5)
for _ in range(5):
    print("test")

for row in range(10):
    for column in range(5):
        print("*", end="")
    print() # go down to the next line

size = int(input("How large of a triangle do you want?"))

for row in range(1, size+1):
    print("*" * row)


# spaces = size - 1
for row in range(1, size+1):
    for space in range(size - row):
    # for space in range(spaces):
        print(" ", end="")
    print("*" * row)
    # spaces -= 1

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(f'{hour:02d}:{minute:02d}:{second:02d}')


choice = input("This, that or quit")

# this works, but Eric thinks it's ugly
while True:
    if choice == "quit":
        break # ends the loop immediately
    # code continues here

while choice != "quit":
    if choice == "this":
        print("do this")


play_again = "y"

while play_again == "y":
    # do project 1


    play_again = input("Play again y/n ?")


for number in range(10):
    if number % 2 == 0:
        continue # loop body ends, jumps to the top
    print(number)

    # range 3rd option is the `counting by`
for number in range(1, 10, 2):
    print(number)

                            # step
for number in range(10, 0, -1):
    print(number)

for number in range(10, 0): # needs the -1
    print(number)

are_you_bored = 'n'

while are_you_bored == "n":
    print("Happy Wednesday")
    are_you_bored = input("are you bored? y/n or quit")
    if are_you_bored == "quit":
        break # if you break, the loop else won't run
else:
    print("Ended normally")


numbers = []

number = 0

while number != -1:
    number = int(input("Enter a number or -1 to stop"))
    if number != -1:
        numbers.append(number)

print(numbers)

for index in range(len(numbers)):
    print(f"numbers list, index {index} value{numbers[index]}")

# gets a copy of the value
for value in numbers:
    value = value + 10
    # doesn't change the value stored IN the list
    print(value)

for index in range(len(numbers)):
    numbers[index] += 10 # this will change the value in the list
    print(numbers[index])

for index, value in enumerate(numbers): # shortcut to get both index and value
    print(f"numbers {index} : value {value}")

print(numbers)






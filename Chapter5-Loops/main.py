import random

max_number = int(input("How high of a number do you want to guess?"))

number_to_guess = random.randint(1, max_number)

guess = int(input(f"Guess a number 1 - {max_number}: "))

# validation loop
while guess < 1 or guess > max_number:
    guess = int(input(f"Guess a number 1 - {max_number}: "))

number_of_guesses = 1
# runs as long as the expression is true
while guess != number_to_guess:

    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")

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


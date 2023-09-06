import math
import random

print('Hello world!')

print("happy wednesday!")

# comments are ignored by python
# this line of code prints 'yay internet' to the screen
# this is wrong now, ope
print("My name is Eric!")

print("Yay internet")

dollars_per_hour = float(input("Enter your hourly wage"))

print("If you make $", dollars_per_hour, "/hour you will make $", dollars_per_hour * 40, "in a week")
print("That makes $", dollars_per_hour*40*52, "per year ( before taxes) !")

first_number = int(input("enter first number"))
second_number = int(input("enter second number"))

print(first_number, "+", second_number, " = ", first_number + second_number)
print(first_number, "-", second_number, " = ", first_number - second_number)
print(first_number, "*", second_number, " = ", first_number * second_number)
print(first_number, "/", second_number, " = ", first_number / second_number)

# // is for integer division
# % is for modulus or modulo, the integer remainder
print(first_number, "/", second_number, " = ", first_number // second_number, "reminder", first_number % second_number)


number_to_square_root = int(input("Enter a number to find the sqrt of"))
print("The sqrt of", number_to_square_root, "is", math.sqrt(number_to_square_root))

print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())

print("random number 1-10", int(random.random()*10 % 10) + 1)
print("random number 1-10", int(random.random()*10 % 10) + 1)
print("random number 1-10", int(random.random()*10 % 10) + 1)
print("random number 1-10", int(random.random()*10 % 10) + 1)
print("random number 1-10", int(random.random()*10 % 10) + 1)

# randint takes low and high values inclusive
print("random number 1-10", random.randint(1, 10))
print("random number 1-10", random.randint(1, 10))
print("random number 1-10", random.randint(1, 10))
print("random number 1-10", random.randint(1, 10))
print("random number 1-10", random.randint(1, 10))


print("Here is your random password")
# setting the end to "" prevents it from going to the next line
print(chr(random.randint(65,90)), end="")
print(chr(random.randint(65,90)), end="")
print(chr(random.randint(65,90)), end="")
print(chr(random.randint(65,90)), end="")
print(chr(random.randint(65,90)))

print("John O'Donnel")
print('Eric said \n"Stop!"')
print("John O'Donnel said \"stop!\"")

shift = int(input("How far should we shift letters?"))
# keep within a range of 26 values, add 65 to get back to capital A
print(chr((ord('E')+shift) % 26 + 65))
print(chr((ord('R')+shift) % 26 + 65))
print(chr((ord('I')+shift) % 26 + 65))
print(chr((ord('C')+shift) % 26 + 65))

first_letter = input("Enter your first letter")
second_letter = input("Enter your second letter")
third_letter = input("Enter your third letter")

result = ord(first_letter) + ord(second_letter) + ord(third_letter)

print("The magic value of that word is", result)

name = input("Enter your name")
print("Hi", name)
# can't use comma separated output in input, like you can in print

# example using print first
# print("How are you today", name, "?")
# feeling = input()
feeling = input("How are you today " + name + "?")
print("Oh that's nice!")

# I got the rounding method from https://umgpt.umich.edu/
# prompt: how do I round a value up in python
print("4.2 rounded up is", math.ceil(4.2))
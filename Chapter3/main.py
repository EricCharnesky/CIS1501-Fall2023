print("Happy Monday!")
print("Welcome to chapter 3")

# add your own new lines
really_long_string = "first line\\n" \
    "second line\n" \
    "third line "

# follows new lines
multi_line_string = """first line
second line
third line
"""

print(really_long_string)
print(multi_line_string)

name = "Eric"
# letter at index 0 - first letter
print(name[0])
print(name[1])
print(name[2])
print(name[3])
# IndexError: string index out of range - no index 4
# print(name[4])

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabet[4], alphabet[17], alphabet[8], alphabet[2])

# strings are immutable - can't change
# but you can change it's entire value
alphabet = 'abcdefghijklmnopqrstuvwxyz'

name = input("enter your name")
favorite_animal = input("Enter your favorite animal")
favorite_vacation_spot = input("Enter your favorite vacation spot")

print(name + "'s favorite animal is", favorite_animal, "and they like to vacation at", favorite_vacation_spot)
print(f"{name}'s favorite animal is {favorite_animal} and they like to vacation at {favorite_vacation_spot}")

hourly_wage = float(input("Enter your hourly wage"))
hours_worked = float(input("Enter the number of hours worked"))

print(f"Your gross pay is ${hours_worked * hourly_wage:.2f}")

# lists are mutable
some_list = ["Joy", "Jeb", "Vivi", "Journey", "Jubilee", "Jackson", "Jasper"]
print(some_list)
some_list[2] = "Jenavieve"
print(some_list)

# get values by index, just like strings
print(some_list[3])

# lists can have different types
crazy_list = [10, 2.5, "ten"]
print(crazy_list[0] * crazy_list[2])
# fails, can't multiply a string by a float
# print(crazy_list[1] * crazy_list[2])

numbers = [1,2,3,4,4,4,4,4,4,5]
print(numbers)
numbers.append(6) # adds to the end
print(numbers)

# remove the first match by value
numbers.remove(4)
print(numbers)

# pop removes by index value, not value value
numbers.pop(1)
print(numbers)

# adds something to be the new value at that index, every else shifts
# puts value 27 at index 3
numbers.insert(3, 27)
print(numbers)

print(f'the smallest value in the list is{min(numbers)}')
print(f'the largest value in the list is{max(numbers)}')
print(f'the sum value in the list is{sum(numbers)}')
print(f'the average value in the list is{sum(numbers) / len(numbers)}')

scores = []

# two lines
score = int(input("Enter a score"))
scores.append(score)

# single line
scores.append(int(input("Enter a score")))

scores.append(int(input("Enter a score")))
scores.append(int(input("Enter a score")))
scores.append(int(input("Enter a score")))

print(f'the smallest value in the list is{min(scores)}')
print(f'the largest value in the list is{max(scores)}')
print(f'the sum value in the list is{sum(scores)}')
print(f'the average value in the list is{sum(scores) / len(scores)}')


classes = ('CIS 1501', 'CIS 2001', 'CIS 350', 'IMSE 317', 'MAT 170')
print(classes[3])
# tuples are immutable - can't change values
#classes[3] = 'Probability and Statistics, with calculus!'

def print_in_title_case(word):
    for index in range(len(word)):
        if index == 0:
            print(word[index].upper(), end="")
        else:
            print(word[index].lower(), end="")
    print()

def is_letter_in_word(letters_guessed):



name = input("Enter your name")

for word in name.split(" "):
    print_in_title_case(word)

print(name.title())

start_index = 0

while name.find(" ", start_index) != -1:
    space_index = name.find(" ", start_index)
    word = name[start_index:space_index]
    start_index = space_index + 1
    print_in_title_case(word)

# loop ends when there are no more spaces found, print the last name
word = name[start_index:]
print_in_title_case(word)



initial = name[0]

# ending index is optional, defaults to the end of the string
last_name = name[5:len(name)]
last_name = name[5:]

# negative counts in from the end
# start index defaults to 0
first_name = name[:-10]

print(first_name)

print(last_name)

for index in range(len(name)):
    if index == 0:
        print(name[index].upper(), end="")
    else:
        print(name[index].lower(), end="")
print()



alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# start index : end index : stride
print(alphabet[::2])
print(alphabet[1::2])

message = input("Enter a message to encode")

print(message[::2] + message[1::2])

first_half = message[::2]
second_half = message[1::2]

for index in range(len(first_half)):
    print(first_half[index], end="")
    print(second_half[index], end="")
print()

names = ["Joy", "Jeb", 'Vivi', 'Journey', 'Jubilee', "Jack", "Jasper"]

print(", ".join(names))

for name in names:
    print(name + ", ", end="")
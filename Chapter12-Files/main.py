import csv

with open("lotto.txt") as lotto_file:
    lines = lotto_file.readlines()
    numbers = []
    for line in lines:
        for number in line.split(" "):
            numbers.append(int(number))

    print(numbers)


file = open("C:/Users/EricC/OneDrive/Documents/GitHub/CIS1501-Fall2023/Chapter12-Files/test.txt")

lines = file.readlines()

file.close()

# each line will have it's own endline already
for line in lines:
    print(line, end="")
print()

# no need to close, the with block does it for us
with open("test.txt") as file:
    lines = file.readlines()

    for line in lines:
        print(line, end="")
    print()

with open("numbers.txt") as numbersFile:
    lines = numbersFile.readlines()
    total = 0
    line_count = 0
    for line in lines:
        if line.strip():
            total += int(line)
            line_count += 1
    print("Average value in files is", total/line_count)

with open('lucky numbers.txt', 'w') as file_to_write:
    file_to_write.write("4\n")
    file_to_write.write("11\n")
    file_to_write.write("23\n")


with open('test.csv') as csv_file:
    lines = csv_file.readlines()
    for line in lines:
        # real bad if you get quoted commas
        cells = line.split(",")
        for cell in cells:
            print(cell, end=" ")


with open('test.csv') as csvfile:
    reader = csv.reader(csvfile)

    row_num = 0
    for row in reader:
        print(f'Row #{row_num}: {row}')
        row_num += 1

numbers = []
for number in range(6):
    numbers.append(int(input("Enter a lotto number")))

with open("lotto.txt", 'a') as lotto_file:
    lotto_file.write(" ".join(str(number) for number in numbers) + "\n")


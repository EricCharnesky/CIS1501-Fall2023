my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# won't change the values in the list
# value is a copy of the value in the list, not the original
for value in my_list:
    value += 10
    print(value)

print(my_list)

# changes the values in the list
for index in range(len(my_list)):
    my_list[index] += 10
    print(my_list[index])

print(my_list)

# slicing - makes a copy
middle_three_values = my_list[3:6]
print(middle_three_values)
for index in range(len(middle_three_values)):
    middle_three_values[index] -= 10

print(middle_three_values)
print(my_list)

# takes a slice from beginning to end
copy_of_my_list = my_list[:]


new_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

# you shouldn't modify a list as you iterate over it
#for index in range(len(new_list)):
#    if new_list[index] % 2 == 0:
#        new_list.remove(new_list[index])

#print(new_list)
# doesn't crash, but skips values as we iterate
for value in new_list:
    if value % 2 != 0:
        new_list.remove(value)

# loop over a copy that doesn't change as we change the original
for value in new_list[:]:
    if value % 2 != 0:
        new_list.remove(value)

print(new_list)

new_list.sort()

print(new_list)

if "":
    print("empty is true")
else:
    print("empty is false")
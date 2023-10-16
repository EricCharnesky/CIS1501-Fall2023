gradebook = {}

# add - if the key doesn't exist
gradebook['Eric'] = {'Grade': 'A'}

# update - if the key does exist
gradebook['Eric'] = {'Grade': 'B'}
gradebook['Eric']['Grade'] = 'B'

gradebook['Jeb'] = {'Grade': 'B'}
gradebook['Vivi'] = {'Grade': 'C'}
gradebook['Journey'] = {'Grade': 'A'}

if 'Jasmine' in gradebook:
    # this method will crash if the key doesn't exist
    print(gradebook['Jasmine'])

# allows you to not crash and give a default
print(gradebook.get('Jasmine', 'N/A'))

# each key will be called name in the loop
for name in gradebook:
    print(name, gradebook[name])

name = ""

while name != "QUIT":

    name = input("Enter a name to add to the gradebook, or QUIT")

    if name != "QUIT":
        # looks for a matching KEY
        if name in gradebook:
            grade = input("Enter the grade to update for " + name)
        else:
            grade = input("Enter the grade to add for " + name)

        gradebook[name] = grade


# will sort the keys before iterating over them
for name in sorted(gradebook.keys()):
    print(name, gradebook[name])
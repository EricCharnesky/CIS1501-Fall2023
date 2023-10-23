from copy import deepcopy


def add_student(gradebook):
    name = input("Enter a student name to add")
    gradebook[name] = {}
    # go and copy assignments from another student

gradebook = {}

gradebook['Eric'] = {}

gradebook['Eric']['Project 0'] = {'score': 0, 'total points': 10}

gradebook['Eric']['Project 1'] = {'score': 0, 'total points': 12}

gradebook['Eric']['Project 2'] = {'score': 0, 'total points': 15}


gradebook['Pedro'] = {}
for assignment in gradebook['Eric']:
    gradebook['Pedro'][assignment] = {'score': 0, 'total points': assignment['total points'] }

print(gradebook)

gradebook['Eric']['Project 0']['score'] = 10
print(gradebook)


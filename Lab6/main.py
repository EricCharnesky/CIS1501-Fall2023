class Assignment:

    def __init__(self, name, points_possible):
        self._name = name
        self._score = 0
        self._points_possible = points_possible

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score

    def get_points_possible(self):
        return self._points_possible

class Student:

    def __init__(self, name):
        self._name = name
        self._assignments = []

    def get_name(self):
        return self._name

    def add_assignment(self, assignment):
        self._assignments.append(assignment)

    def get_assignments(self):
        return self._assignments

class Gradebook:

    def __init__(self, class_name):
        self._class_name = class_name
        self._students = []

    def add_student(self, student):
        # copy assignments from another student
        self._students.append(student)

    def add_assignment(self, assignment):
        # add assignment to each student in list
        for student in self._students:
            student.add_assignment(assignment)

    def score_assignment(self, assignment_name):
        # loop through each student, try and find the assignment that matches the name and then get the score

    def get_students(self):
        return self._students


cis1501 = Gradebook("CIS 1501")

choice = input("Add student, add assignment, score assignment")

if choice == "Add student":
    name = input("Enter the student's name")


elif choice == "add assignment":
    assignment_name = input("Enter the assignment name")
    points_possible = int(input("How many points possible"))
    assignment = Assignment(assignment_name, points_possible)
    cis1501.add_assignment(assignment)


for student in cis1501.get_students():
    print(student.get_name())
    for assignment in student.get_assignments():
        print("Assignment", assignment.get_name())
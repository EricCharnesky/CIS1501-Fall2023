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

    def set_name(self, name):
        self._name = name

    def add_assignment(self, assignment):
        self._assignments.append(assignment)

    def get_assignments(self):
        return self._assignments


class Gradebook:

    def __init__(self, class_name):
        self._class_name = class_name
        self._students = []

    def add_student(self, student):
        self._students.append(student)
        if len(self._students) != 1: # if it's 1, it's the first student
            student_to_copy = self._students[0]
            for assignment_to_copy in student_to_copy.get_assignments():
                # makes a new assignment to avoid getting a copy of the score
                copy = Assignment(assignment_to_copy.get_name(), assignment_to_copy.get_points_possible())
                student.add_assignment(copy)

    def add_assignment(self, assignment):
        # add assignment to each student in list
        for student in self._students:
            student.add_assignment(assignment)

    def score_assignment(self, assignment_name):
        for student in self._students:
            for assignment in student.get_assignments():
                if assignment.get_name() == assignment_name:
                    score = int(input("Enter the score for " + student.get_name() +
                                      " - total points possible: " + str(assignment.get_points_possible())))
                    assignment.set_score(score)

    def get_students(self):
        return self._students


cis1501 = Gradebook("CIS 1501")
cis1501.add_student("Eric")
cis1501.get_students()[0].add_assignment("test 1", 10)
cis1501.get_students()[0].get_assignments()[0].set_score(10)

student_list = cis1501.get_students()
first_student = student_list[0]
first_student.add_assignment("test 2", 10)

choice = ""

while choice != "quit":

    if choice == "add student":
        name = input("Enter the student's name")
        new_student = Student(name)
        cis1501.add_student(new_student)

    elif choice == "add assignment":
        assignment_name = input("Enter the assignment name")
        points_possible = int(input("How many points possible"))
        assignment = Assignment(assignment_name, points_possible)
        cis1501.add_assignment(assignment)

    elif choice == "score assignment":
        assignment_name = input("Enter the assignment name")
        cis1501.score_assignment(assignment_name)

    choice = input("Add student, add assignment, score assignment, or quit").lower()



for student in cis1501.get_students():
    print(student.get_name())
    for assignment in student.get_assignments():
        print("Assignment", assignment.get_name(), "score", assignment.get_score(), "out of", assignment.get_points_possible())
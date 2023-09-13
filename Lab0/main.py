import math

# constant value - constant variable
COST_PER_CREDIT = 606
COST_PER_SEMESTER_MAX = 7272

credits_required_for_degree = int(input("How many credits do you need?"))
credits_completed = int(input("How many credits do you have completed?"))
average_credits_per_semester = int(input("how many credits do you take per semester?"))

credits_remaining = credits_required_for_degree - credits_completed

print("you have", math.ceil(credits_remaining / average_credits_per_semester ), "semesters left" )

print("If you are taking less than 12 credits per semester, it will cost about $",
      credits_remaining * COST_PER_CREDIT)

print("if you are taking more than 12 credits per semester, it will cost about $",
      math.floor(credits_remaining / average_credits_per_semester) * COST_PER_SEMESTER_MAX +
      ( credits_remaining % average_credits_per_semester ) * COST_PER_CREDIT )

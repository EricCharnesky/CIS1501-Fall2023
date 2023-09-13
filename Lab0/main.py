import math

# constant value - constant variable
COST_PER_CREDIT = 606
COST_PER_SEMESTER_MAX = 7272

credits_required_for_degree = int(input("How many credits do you need?"))
credits_completed = int(input("How many credits do you have completed?"))
average_credits_per_semester = int(input("how many credits do you take per semester?"))

credits_remaining = credits_required_for_degree - credits_completed

print("you have", math.ceil(credits_remaining / average_credits_per_semester ), "semesters left" )

if average_credits_per_semester < 12:
      print("If you are taking less than 12 credits per semester, it will cost about $",
            credits_remaining * COST_PER_CREDIT)
      print("more code that runs if average is < 12")
else:
      print("if you are taking more than 12 credits per semester, it will cost about $",
            math.floor(credits_remaining / average_credits_per_semester) * COST_PER_SEMESTER_MAX +
            ( credits_remaining % average_credits_per_semester ) * COST_PER_CREDIT )

# use .lower() to make the string all lower case
year_in_school = input("Enter your year in school (Freshman, Sophomore, Junior, Senior)").lower()

if year_in_school == "freshman":
      print("Welcome to UMD!")
elif year_in_school == "sophomore":
      print("Hope you found some cool clubs to join")
elif year_in_school == "junior":
      print("Did you have an internship yet?")
elif year_in_school == "senior":
      print("You're almost done!")
else:
      print("I don't know what you entered")

import random


def get_random_value_negative_ten_to_ten():
    return random.randint(-10, 10)


def get_valid_command():
    command = ""

    while command != "x+" and command != "x-" \
            and command != "y+" and command != "y-" \
            and command != "thrusters" and command != "self destruct" \
            and command != "nothing":
        command = input("Enter x+, x-, y+, y-, thrusters, self destruct, or nothing").lower()

    return command


def self_destruct():
    cancellation_code = ""
    while cancellation_code != "1501":
        cancellation_code = input("Self destruct sequence activated, enter cancellation code")

    print("Self destruct aborted")


def display_status(distance_from_surface, x_tilt, y_tilt):
    print("Distance from surface is", distance_from_surface)
    print(f'X tilt: {x_tilt} - Y tilt: {y_tilt}')



def display_landing_status(x_tilt, y_tilt):
    # if x_tilt != 0 or y_tilt != 0:
    if x_tilt or y_tilt: # shortcut for x and y are non 0 values
        print("You crashed the 3 billion dollar lander, uh oh!")
    else: # both x and y must be 0
        print("You landed successfully, enjoy the moon!")


def get_lander_to_surface(x_tilt, y_tilt):
    distance_from_surface = 10

    while distance_from_surface > 0:
        display_status(distance_from_surface, x_tilt, y_tilt)

        command = get_valid_command()

        if command == "x+":
            x_tilt += 1
        elif command == "x-":
            x_tilt -= 1
        elif command == "y+":
            y_tilt += 1
        elif command == "y-":
            y_tilt -= 1
        elif command == "thrusters":
            distance_from_surface += 2
        elif command == "self destruct":
            self_destruct()

        distance_from_surface -= 1

    display_landing_status(x_tilt, y_tilt)


play_again = 'y'

while play_again.lower() == "y":

    x_tilt = get_random_value_negative_ten_to_ten()
    y_tilt = get_random_value_negative_ten_to_ten()

    get_lander_to_surface(x_tilt, y_tilt)

    play_again = input("Do you want to play again? y/n")
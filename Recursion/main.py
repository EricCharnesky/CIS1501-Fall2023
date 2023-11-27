def count_down(number):
    if number > 0:
        print(number)
        count_down(number - 1)
    else:
        print("Blastoff!")

def fibonacci(nth):
    if nth <= 2:
        return 1
    return fibonacci(nth - 1) + fibonacci(nth - 2)

def better_fib(nth):
    if nth <= 2:
        return 1

    previous = 1
    current = 1
    current_nth = 2

    while current_nth < nth:
        next = previous + current
        previous = current
        current = next
        current_nth += 1

    return current



for nth in range(40):
    print(nth, ":", better_fib(nth))

count_down(10)
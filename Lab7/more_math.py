def fibonacci(nth):
    if nth < 1:
        raise ValueError("Invalid nth term")
    if nth < 3:
        return 1
    previous = 1
    current = 1
    current_nth = 2
    while current_nth != nth:
        next = previous + current
        previous = current
        current = next
        current_nth += 1
    return current
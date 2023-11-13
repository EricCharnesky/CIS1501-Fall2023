import random


class PowerBallTicket:

    def __init__(self, values=None):
        if values:
            if len(values) != 6:
                raise ValueError("Invalid ticket")
            for value in values[:5]:
                if not ( 1 <= value <= 69 ):
                    raise ValueError("Invalid numbers")
                if values[:5].count(value) != 1:
                    raise ValueError("No duplicates allowed")
            if not ( 1 <= values[5] <= 26 ):
                raise ValueError("Invalid numbers")
            self._values = values[:]
        else:
            self._values = random.sample(range(1, 70), 5)
            self._values.append(random.randint(1, 26))

    def get_values(self):
        return self._values[:] # make a copy to keep it from changing

    def get_winnings(self, winning_ticket):
        number_of_white_matches = len(set(self._values[:5]).intersection(winning_ticket.get_values()[:5]))
        red_matches = self._values[5] == winning_ticket.get_values()[5]

        if number_of_white_matches == 5 and red_matches:
            return 235_000_000
        if number_of_white_matches == 5:
            return 1_000_000
        if number_of_white_matches == 4 and red_matches:
            return 50_000
        if (number_of_white_matches == 4
                or number_of_white_matches == 3 and red_matches):
            return 100
        if (number_of_white_matches == 3
                or number_of_white_matches == 2 and red_matches):
            return 7
        if red_matches:
            return 4
        return 0

    def __str__(self):
        return " ".join(str(number) for number in self._values)


ticket = PowerBallTicket()
another_ticket = PowerBallTicket()

print(ticket.get_winnings(another_ticket))
print(ticket)
print(another_ticket)

with open("lotto.txt", 'a') as lotto_file:
    for ticket in range(100):
        ticket = PowerBallTicket()
        lotto_file.write(str(ticket) + "\n")

with open("lotto.txt") as lotto_file:
    total_winnings = 0
    winning_ticket = PowerBallTicket()
    lines = lotto_file.readlines()
    for line in lines:
        values = line.split(" ")
        numbers = []
        for value in values:
            numbers.append(int(value))
        ticket = PowerBallTicket(numbers)
        total_winnings += ticket.get_winnings(winning_ticket)
        total_winnings -= 2

    print(f"You bought {len(lines)} tickets and your total winnings is: {total_winnings}")
import random

# https://www.programiz.org/1237/python-program-to-check-prime-number-using-function
def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    """
    if n < 2:  # 0 and 1 are not primes
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factorial_plus_odds_minus_evens(n):
    total = 1
    for number in range(2, n+1):
        if is_prime(number):
            total *= number
        if number % 2: # odd
            total += number
        else:
            total -= number
    return total


def bad_hash(some_string):
    total = 0
    for letter in some_string:
        total += ord(letter)
    return total


def verify_bad_hash(some_string, some_hash_value):
    return bad_hash(some_string) == some_hash_value


def vowel_count_sometimes_y(some_word):
    vowel_count = 0
    some_word = some_word.upper()
    for letter in some_word:
        if letter in 'AEIOU':
            vowel_count += 1
        elif letter == "Y":
            if random.randint(1,10) % 2:
                vowel_count += 1
    return vowel_count


for value in range(1, 10):
    print(prime_factorial_plus_odds_minus_evens(value))

name = "Eric"
hash_value = bad_hash(name)
print("Verified: ", verify_bad_hash(name, hash_value))


for iteration in range(10):
    print(vowel_count_sometimes_y("Happy Monday!"))

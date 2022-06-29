#   Guess the number for the computer produced secret number
"""
PSEUDO RUN
    Import the random function module
    Randomize a number within boundary limit
    Guess the number at user end
    Compare and print result
"""
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Print a number between 1 and {x}: '))
        if guess < random_number:
            print(f"Guessed a little lower. Try again")
        elif guess > random_number:
            print(f"Guessed a little higher. Try again")
        else:
            print(f'Congratulations, you guessed the correct number')

guess(10)
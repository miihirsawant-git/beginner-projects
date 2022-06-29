#   Guess the number game

import random

print(f'\nGuess game\n')
print(f'1. Do you want to guess my secret number\n2. Should I guess your secret number')
choice = int(input(f'\nSelect a choice: '))

def user_guess(x):
        random_number = random.randint(1, x)
        guess = 0
        while guess != random_number:
            guess = int(input(f'\nGuess a number between 1 and {x}: '))
            if guess < random_number:
                print(f"Guessed a little lower. Try again")
            elif guess > random_number:
                print(f"Guessed a little higher. Try again")
            else:
                print(f'\n\n\nCongratulations, you guessed the correct number!\n\n\n')

def computer_guess(x):
        low = 1
        high = x
        feedback = ''
        while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = high
            feedback = input(f'\nIs the {guess} too high (H),low (L) or correct (C)? ').lower()
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1

        print(f'\n\n\nThe computer has guessed your number, {guess}, correctly!\n\n\n')

if choice == 1:
    user_guess(100)
elif choice == 2:
    computer_guess(100)
else:
    print(f'Incorrect entry')
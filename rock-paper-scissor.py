# Rock-Paper-Scissor Game

import random

def game():

    print('\n\nRock-Paper-Scissor Game\n\n')
    user_choice = input(f'Select a choice: [R]ock [P]aper or [S]cissor:     ').lower()
    computer_choice = random.choice([ 'r', 'p', 's'])

    # r > s, s > p, p > r

    if user_choice == computer_choice:
        return 'tie'

    if (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r'):
        return 'You won!'

    return 'You lost!'

print(game())

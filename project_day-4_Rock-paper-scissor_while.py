from os import system
from random import randint, random

system('clear')

game_sets = 0
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

while game_sets < 3:
    user_input = int(input('Type 0 for Rock, 1 for Paper or 2 for Scissors.\nWhat do you choose? '))
    game_sets += 1

    if user_input == 0:
        print(rock)

    elif user_input == 1:
        print(paper)

    elif user_input == 2:
        print(scissor)

    else: 
        print('That is not an option!!')

    print('Computer Choose:')
    random_int = randint(0, 2)

    if random_int == 0:
        print(rock)

    elif random_int == 1:
        print(paper)

    elif random_int == 2:
        print(scissor)
    
    else: 
        print('...')
    

    if user_input == random_int:
        print('\tIs a tie!\n')
    elif (user_input == 0 and random_int == 2) or (user_input == 1 and random_int == 0) or (user_input == 2 and random_int == 1):
        print('\tYou win\n')
    else: 
        print('\tYou Lose\n')
       

print('\nThanks for play, goodbye')
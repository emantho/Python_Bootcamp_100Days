from os import system
from random import randint, random

system('clear')

input = int(input('Type 0 for Rock, 1 for Paper or 2 for Scissors.\nWhat do you choose? '))

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

if input == 0:
    print(rock)

elif input == 1:
    print(paper)

elif input == 2:
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

# if input == 0:
#     print('Is a tie!')
# elif input == 
# #print('You win')
# #print('You Lose')

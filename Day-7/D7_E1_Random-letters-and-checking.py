from mimetypes import guess_all_extensions
from os import system ; system("clear")
import random

word_list = ['Angel', 'Ojo', 'Pizza', 'Enojado', 'Fuego']

# TODO-1 - Radomly choose a word from the word_list and assing it to a variable called chosen_word.

chosen_word = random.choice(word_list)
#print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assing their answer to a variable called guess. Make Guess lower case
# guess = ""
# for n in range(len(chosen_word)):
#     user = input("Write a letter to guess the word: ")
#     guess += user
# print(guess)
guess = input("Write a letter to guess the word: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) in one of the letter in the chosen_word

for l in chosen_word.lower():
    if guess == l:
        print(f"Correct")
    else:
        print(f"Incorrect")
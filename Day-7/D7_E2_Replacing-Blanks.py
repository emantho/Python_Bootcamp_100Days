# from os import system ; system("clear")
import random

word_list = ['Ojo', 'Pizza', 'analfabeto', 'Angel', 'Enojado', 'Fuego']

# TODO-1 - Radomly choose a word from the word_list and assing it to a variable called chosen_word.
chosen_word = random.choice(word_list)
chosen_word = chosen_word.lower()
print(chosen_word)

# Adding a "_" for each letter space
guessed_word = []
for _ in range(len(chosen_word)):
    guessed_word.append("_")


# TODO-2 - Ask the user to guess a letter and assing their answer to a variable called guess. Make Guess lower case
guess = input("Write a letter to guess the word: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) in one of the letter in the chosen_word
    # replacing empty spaces
chosen_word = list(chosen_word) # string to list
word_count = chosen_word.count(guess)

for wc in range(word_count):
    word_index = chosen_word.index(guess)
    guessed_word[word_index] = guess
    chosen_word[word_index] = "#"
print(guessed_word)

# # ------ Another solution --------- #
# for position in range(len(chosen_word)):
#     letter = chosen_word[position]  # use string positions
#     if letter == guess:
#         guessed_word[position] = letter
# print(guessed_word)
# # ------ Another solution --------- #

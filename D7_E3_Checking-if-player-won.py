# from os import system ; system("clear")
import random

word_list = ['Ojo', 'Pizza', 'analfabeto', 'Angel', 'Enojado', 'Fuego']

# Radomly choose a word from the word_list and assing it to a variable called chosen_word.
chosen_word = random.choice(word_list)
chosen_word = chosen_word.lower()
print(f"Hint: The word to guess is: {chosen_word}")
chosen_word = list(chosen_word) # string to list

# Adding a "_" for each letter space
guessed_word = []
for _ in range(len(chosen_word)):
    guessed_word.append("_")
print(guessed_word)

# TODO-1 - Adding loop to make repetitive the game

while "_" in guessed_word:#control_word != guessed_word:
    # Ask the user to guess a letter and assing their answer to a variable called guess. Make Guess lower case
    guess = input("Write a letter to guess the word: ").lower()

    # Check if the letter the user guessed (guess) in one of the letter in the chosen_word
        # replacing empty spaces
    word_count = chosen_word.count(guess)

    for wc in range(word_count):
        word_index = chosen_word.index(guess)
        guessed_word[word_index] = guess
        chosen_word[word_index] = "#"
    print(f"\n{guessed_word}")
    
print("Congrats, you WIN !!!!")
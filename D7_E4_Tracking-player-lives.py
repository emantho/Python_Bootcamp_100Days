from os import system ; system("clear")
import random

# stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /    |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''']


# list of words to guess
word_list = ['Ojo', 'Pizza', 'analfabeto', 'Angel', 'Enojado', 'Fuego']

# Radomly choose a word from the word_list and assing it to a variable called chosen_word.
chosen_word = random.choice(word_list)
chosen_word = chosen_word.lower()
message = f"\nThe word to guess was: {chosen_word}"
chosen_word = list(chosen_word) # string to list

# Adding a "_" for each letter space
guessed_word = []
for _ in range(len(chosen_word)):
    guessed_word.append("_")

print_word = ''.join(guessed_word) # list to string OJO
print(print_word)

# TODO-1 - Adding loop to make repetitive the game
game_over = True
tries = 6
while game_over: #control_word != guessed_word:
    # Ask the user to guess a letter and assing their answer to a variable called guess. Make Guess lower case
    guess = input("\nWrite a letter to guess the word: ").lower()

    # Check if the letter the user guessed (guess) in one of the letter in the chosen_word
        # replacing empty spaces
    word_count = chosen_word.count(guess)
    
    if guess in chosen_word:
        for wc in range(word_count):
            word_index = chosen_word.index(guess)
            guessed_word[word_index] = guess
            chosen_word[word_index] = "#"
        print("\nLook nice")
        print(f"\nThe word is: {''.join(guessed_word)}")

        if "_" not in guessed_word:
            print("CONGRATULATIONS, YOU WIN !!!!")
            game_over = False
    
    else: 
        tries -= 1
        print("Oh no...")
        print(stages[tries])
        print(f"\n{''.join(guessed_word)}")
        if tries == 0:
            print(f"\n :( YOU LOSE :( ")
            print(message)
            game_over = False
    

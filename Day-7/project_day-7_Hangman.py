from os import system ; system("clear")
import random
import my_module_words
import my_mod_HangmanArts

print(my_mod_HangmanArts.hangman_title)

# Choosing radonmly a word from list
#chosen_word = random.choice(my_module_words.words)
chosen_word = "ojo"
chosen_word = chosen_word.lower()
message = f"Hidden Word is: {chosen_word}"

# creating "_" list
guessed_word = []
for _ in range(len(chosen_word)):
    guessed_word.append("_")

# list into string
print(''.join(guessed_word))

# while word hasn't been discovered or user lives don't reach 0
gameOn = True
userLives = 6
chosen_word = list(chosen_word)

while gameOn:
    # Asking user for a letter
    if "_" in guessed_word and userLives != 0:
        guess_word = input("\nEnter a letter: ").lower()
        count_word = chosen_word.count(guess_word)

        system("clear")

        # Cheking letter in chosen_word
        if guess_word in chosen_word:
            for num in range(count_word):
                index_word = chosen_word.index(guess_word)
                guessed_word[index_word] = guess_word
                chosen_word[index_word] = "#"
            print(''.join(guessed_word))

        elif guess_word not in chosen_word:
            
            if guess_word in guessed_word:
                print(f"The letter {guess_word} was introduce already")
                print(''.join(guessed_word))
            else: 
                print(f"You guessed {guess_word}, that's not in the Word.\nYou lose a life.")
                userLives -= 1
                print(''.join(guessed_word))
                print(my_mod_HangmanArts.stages[userLives])
                
    elif "_" not in guessed_word:
        print(my_mod_HangmanArts.winner)
        gameOn = False
        
    elif userLives == 0:
        print(message)
        print(my_mod_HangmanArts.loser)
        gameOn = False
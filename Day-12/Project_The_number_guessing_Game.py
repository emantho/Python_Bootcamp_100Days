from os import system
from D12_art import logo
import random

system("Clear")


def random_number():
    to_guess = random.randint(1, 100)
    return to_guess


def game_dificult(user_difficulty):
    if user_difficulty == "easy":
        attemps = 10
        return attemps
    elif user_difficulty == "hard":
        attemps = 5
        return attemps


# main program start
new_game = "y"
while new_game == "y":
    system("clear")
    user_attemps = 0

    print(logo)

    print("I'm thinking in a number between 1 to 100.")

    while True:
        user_diff_chosed = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if user_diff_chosed != "easy" and user_diff_chosed != "hard":
            print(f"{user_diff_chosed} That's not an option")
        else:
            break

    attemps_message = print(
        f"You have {game_dificult(user_diff_chosed)} attemps remaining to guess the number."
    )
    inner_game = True
    to_guess = random_number()

    while inner_game:
        user_guess = int(input("Make a guess: "))
        user_attemps += 1
        if game_dificult(user_diff_chosed) == user_attemps:
            print(f"YOU LOSE !! ")
            print(f"The hidden number is: {to_guess}")
            inner_game = False
        else:
            if user_guess == to_guess:
                print(f"YOU WIN !! ")
                inner_game = False
            elif user_guess < to_guess:
                print("Too low")
            elif user_guess > to_guess:
                print("Too high")

    new_game = input("Wanna play again? Type 'y' or 'n': ")
    if new_game == "n":
        break
# main program end

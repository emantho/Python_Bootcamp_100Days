from os import system

system("clear")
from D11_art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_card = []
dealer_total = 0
player_card = []
player_total = 0
dealer_card_lenght = 1
player_card_lenght = 2

# Pick a card from Cards list
def card_choise(cards_to_choise):
    """Pick a Card from Cards List"""
    return random.choice(cards_to_choise)


# Add all card numbers from lists and create a total
def total_played(played_cards):
    """Make a copy of the list of cards and extract each
    item to create a total of it"""

    total_sum = 0

    for card in played_cards:
        total_sum += card

    return total_sum


# Create list of cards of dealer
def dealer_card_list(card_lenght):
    """Create list of cards of dealer using the length of list"""
    for c in range(card_lenght):
        picked_cards = card_choise(cards)
        dealer_card.append(picked_cards)
    return dealer_card


# Create list of cards of dealer
def player_card_list(card_lenght):
    """Create list of cards of player using the length of list"""
    for c in range(card_lenght):
        picked_cards = card_choise(cards)
        player_card.append(picked_cards)
    return player_card


# -------------- END FUNCTIONS -------------------

# -------------- START PROGRAM --------------------
game_on = input("Do you want to play BlackJack, type 'y' or 'n' to exit: ")
system("clear")
while True:
    print(logo)
    dealer_card = []
    dealer_total = 0
    player_card = []
    player_total = 0
    dealer_card_lenght = 1
    player_card_lenght = 2
    hit = ""
    while game_on == "y":

        if game_on == "y" and hit == "y":
            # Computing total
            player_card_list(player_card_lenght)
            player_total = total_played(player_card)

            # Mesagge of cards and scores
            print(f"Your Cards: {player_card}, current score: {player_total}")

            if player_total <= 21:
                hit = input("\nType 'y' to get another card, type 'n' to pass: ")

            else:
                hit = "n"
                game_on = ""
                print("\nYOU LOSE\n")

        elif game_on == "y" and hit == "n":
            while dealer_total <= 21:

                dealer_card_list(dealer_card_lenght)
                dealer_total = total_played(dealer_card)

                if player_total < dealer_total and 17 <= dealer_total <= 21:
                    print(
                        f"Computer's cards: {dealer_card}, current score: {dealer_total}"
                    )
                    hit = "n"
                    game_on = ""
                    print("\nYOU LOSE\n")
                    break

                elif dealer_total == player_total:
                    hit = "n"
                    game_on = ""
                    print("\nIS A DRAW\n")
                    break

                elif dealer_total > 21:
                    print(
                        f"Computer's cards: {dealer_card}, current score: {dealer_total}"
                    )
                    hit = "n"
                    game_on = ""
                    print("\nYOU WIN\n")
                    break

        elif game_on == "y":
            # computing computer game
            dealer_card_list(dealer_card_lenght)
            dealer_total = total_played(dealer_card)

            # Computing total
            player_card_list(player_card_lenght)
            player_total = total_played(player_card)

            # Mesagge of cards and scores
            print(f"Computer's first card: {dealer_card}")
            print(f"Your Cards: {player_card}, current score: {player_total}")

            # asking player to hit
            hit = input("\nType 'y' to get another card, type 'n' to pass: ")
            if hit == "y":
                player_card_lenght = 1

    game_on = input("Do you want to play again, type 'y' or 'n' to exit: ")
    system("clear")
    if game_on == "n":
        print("Goodbye")
        break

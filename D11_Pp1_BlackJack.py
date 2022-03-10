from os import system ; system("clear")
from D10_art import logo
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

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
    to_sum_cards = played_cards.copy()
    total_sum = 0
    for card in range(len(to_sum_cards)):
        total_sum += to_sum_cards.pop()
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

# --------------END FUNCTIONS -------------------

# -------------- START PROGRAM --------------------
game_on = True
while game_on:
    
    # Computing total
    dealer_total = total_played(dealer_card)
    player_total = total_played(player_card)
    
    # creating computer and player card list
    dealer_card_list(dealer_card_lenght)
    player_card_list(player_card_lenght)

    
    # Mesagge of cards and scores
    print(f"Computer's first card: {dealer_card}")
    print(f"Your Cards: {player_card}, current score: {player_total}")

    # asking player to hit
    hit = input("Type 'y' to get another card, type 'n' to pass: ")
    if hit == 'y':
        print()


 # print(f"Computer's first card: {dealer_card}, current score: {dealer_total}")
# print(f"Your Cards: {player_card}, current score: {player_total}")

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

def card_choise(cards_to_choise):
    return random.choice(cards_to_choise)

def total_played(played_cards):
    to_sum_cards = played_cards.copy()
    total_sum = 0
    for card in range(len(to_sum_cards)):
        total_sum += to_sum_cards.pop()
    return total_sum

def dealer_card_list(card_lenght):#,picked_cards):
    for c in range(card_lenght):
        picked_cards = card_choise(cards)
        dealer_card.append(picked_cards)
        #dealer_card.append(picked_cards)
    return dealer_card

def player_card_list(card_lenght):#,picked_cards):
    for c in range(card_lenght):
        picked_cards = card_choise(cards)
        player_card.append(picked_cards)
        #player_card.append(picked_cards)
    return player_card

# Generating random cards for players
#card_picked_dealer = card_choise(cards)
#card_picked_player = card_choise(cards)

# showing initial cards and totals
dealer_card_list(dealer_card_lenght)#card_picked_dealer,)
player_card_list(player_card_lenght)#card_picked_player,)

dealer_total = total_played(dealer_card)
player_total = total_played(player_card)

print(f"cards from {dealer_card}, total {dealer_total}")
print(f"cards from {player_card}, total {player_total}")

# asking player to hit 
hit = input("Type 'y' to get another card, type 'no' to pass: ")
if hit == 'y':
    player_card_lenght = 1
    player_card_list(player_card_lenght)#card_picked,
    player_total = total_played(player_card)

print(f"cards from {dealer_card}, total {dealer_total}")
print(f"cards from {player_card}, total {player_total}")
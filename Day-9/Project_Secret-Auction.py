# from replit import clear
from os import system

system("clear")
from D9_Art import logo

# HINT: You can call clear() to clear the output in the console.


def check_winner(aucters_list):
    winner = 0
    for i in aucters_list:
        if winner <= aucters_list[i]:
            winner = aucters_list.get(i)
            winner_name = i

    print(f"The winner is: {winner_name} with ${winner}")


aucters = {}
auction = True

print(logo)

while auction:
    aucter_name = input("What your name?: ")
    aucter_bid = int(input("What is your bid: "))
    aucters[aucter_name] = aucter_bid

    auction_round = input(
        "\nAre there any other bidders? Type 'yes' or 'no'.\n"
    ).lower()

    if auction_round == "no":
        check_winner(aucters)
        auction = False

    else:
        system("clear")

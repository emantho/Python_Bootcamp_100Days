
from os import system
# Initial resources
water = 300
milk = 200
coffee = 100
coins = 0

# TODO -A -> Define drinks
def espresso():
    print(f"Here is your Espresso ☕. Enjoy!!")

def latte():
    print(f"Here is your Latte ☕. Enjoy!!")

def cappuccino():
    print(f"Here is you Cappuccino ☕. Enjoy!!")

# TODO -B -> Define report
def report(water_final,milk_final,coffee_final, coins_final):

    print(f"Water: {water_final}ml")
    print(f"Milk: {milk_final}ml")
    print(f"Coffee: {coffee_final}gr")
    print(f"Money: ${coins_final}")

# TODO -C -> Compile a preparation function to do code shorter

# TODO -D -> Compile coin calculator 
    #quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def coin_counter():#c_quarter, c_dime, c_nickle, c_pennie):
    c_quarter = float(input("How many quarters? "))
    c_dime = float(input("How many dime? "))
    c_nickle = float(input("How many nickle? "))
    c_pennie = float(input("How many pennie? "))
    total = c_quarter * 0.25 + c_dime * 0.10 + c_nickle * 0.05 + c_pennie * 0.01
    return total

system("clear")
coffee_maker_on = True
while coffee_maker_on:
    # TODO 1 - Ask user for drink to make
    user_choice = input(" What would you like? (Espresso/Latte/Capuccino): ").lower()

    # TODO 2 - Make report and coffee machine power off
    if user_choice == "report" or user_choice == "off":
        if user_choice == "report":
            report(water, milk, coffee, coins)
            
        elif user_choice == "off":
            coffee_maker_on = False

    # TODO 3 - Create drinks and resources check
    elif user_choice == "espresso":
        e_water,e_milk,e_coffee = 50,0,18 #, p:1.5
        if water < e_water:
            print(f"sorry there is not enough Water.")
        elif milk < e_milk:
            print(f"sorry there is not enough Milk.")
        elif coffee < e_coffee:
            print(f"sorry there is not enough Coffee.")
        else: 
            
            print("Please insert coins")
            total_coins = coin_counter()
            if total_coins >= 1.5:
                water -= e_water
                milk -= e_milk
                coffee -= e_coffee
                print(f"Here is ${total_coins-1.5:.2f} in change.")
                coins += 1.5
                espresso()
            else:
                print("Sorry that's not enough money. Money refunded.")
                #break
        
    elif user_choice == "latte":
        l_water,l_milk,l_coffee = 200,150,24 # p:2.5
        if water < l_water:
            print(f"sorry there is not enough Water.")
        elif milk < l_milk:
            print(f"sorry there is not enough Milk.")
        elif coffee < l_coffee:
            print(f"sorry there is not enough Coffee.")
        else: 
            
            print("Please insert coins")
            total_coins = coin_counter()
            if total_coins >= 2.5:
                water -= l_water
                milk -= l_milk
                coffee -= l_coffee
                print(f"Here is ${total_coins-2.5:.2f} in change.")
                coins += 2.5
                latte()
            else:
                print("Sorry that's not enough money. Money refunded.")
                #break

    elif user_choice == "cappuccino":
        c_water,c_milk,c_coffee = 250,100,24 # p:3.0
        if water < c_water:
            print(f"sorry there is not enough Water.")
        elif milk < c_milk:
            print(f"sorry there is not enough Milk.")
        elif coffee < c_coffee:
            print(f"sorry there is not enough Coffee.")
        else: 
            
            print("Please insert coins")
            total_coins = coin_counter()
            if total_coins >= 3.0:
                water -= c_water
                milk -= c_milk
                coffee -= c_coffee
                print(f"Here is ${total_coins-3.0:.2f} in change.")
                coins += 3.0
                cappuccino()
            else:
                print("Sorry that's not enough money. Money refunded.")
                #break

    



    # TODO - Ask user insert coins
    # TODO - 
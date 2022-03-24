from os import system; system("clear")
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects
coffee_menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

# # Reports
# coffee_machine.report()
# money_machine.report()

while is_on:
    option = coffee_menu.get_items()
    user_choice = input(f" What would you like? {option}: ").lower()

    if user_choice == "report":
        # TODO-1 -> print reports
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        print("GoodBye")
    else: 
        # TODO-2 -> check sufficient ingredients
        drink = coffee_menu.find_drink(option)
        # TODO-3 process coins $ Check transactions successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            
            



# elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
#     sufficient = coffee_machine.is_resource_sufficient(user_choice)
#     print(sufficient)
    # if sufficient:
    #     
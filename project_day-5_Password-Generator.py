from os import system
import random

system("clear")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#final_password = []
final_password = ""

for i in range(0,nr_letters):
    #final_Password.append(random.choice(letters))
    final_password += random.choice(letters)

for i in range(0,nr_symbols):
    #final_Password.append(random.choice(symbols))
    final_password += random.choice(symbols)

for i in range(0,nr_numbers):
    #final_Password.append(random.choice(numbers))
    final_password += random.choice(numbers)

print(f"The Easy Level password is: {final_password}")


# -------------------------------------------------------------
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total_long = nr_letters + nr_symbols + nr_numbers
hard_password = ""

for i in range(0, total_long):
    if i < nr_letters or i < nr_symbols or i < nr_numbers:
        if i < nr_letters:
            hard_password += random.choice(letters)
        elif i < nr_symbols:
            hard_password += random.choice(symbols)
        elif i < nr_numbers:
            hard_password += random.choice(numbers)

print(hard_password)


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


final_password = []
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
game_step = 0

for i in range(0,total_long):
    
    if game_step < nr_letters:
        hard_password += random.choice(letters)
        #print(hard_password)
    if game_step < nr_symbols:
        hard_password += random.choice(symbols)
        #print(hard_password)
    if game_step < nr_numbers:
        hard_password += random.choice(numbers)
        #print(hard_password)
    game_step += 1
print(f"The Hard Level Password is: {hard_password}")

# Other solution done for tutor

final_password1 = []
ultimate_pass = ""

for i in range(0,nr_letters):
    final_password1.append(random.choice(letters))
    
for i in range(0,nr_symbols):
    final_password1.append(random.choice(symbols))
    
for i in range(0,nr_numbers):
    final_password1.append(random.choice(numbers))
        
#print(final_password1)
random.shuffle(final_password1)
#print(f"The Easy Level password is: {final_password1}")

for let in final_password1:
    ultimate_pass += let

print(f"The other solution of Hard Password is: {ultimate_pass}")















# # using string to generate characters 

# import string
# chars = string.ascii_uppercase + string.digits

# print(string.ascii_uppercase)
# print(string.digits)
# print(chars)


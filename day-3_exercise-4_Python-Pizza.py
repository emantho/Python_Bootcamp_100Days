from os import system
system('cls')

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
size = size.lower()
add_pepperoni = add_pepperoni.lower()
extra_cheese = extra_cheese.lower()

if size == 's':
    bill = 15
    print('')
elif size == 'm':
    bill = 20
    print()
elif size == 'l':
    bill = 25
    print()

if size == 's':
    if add_pepperoni == 'y' and extra_cheese == 'y':
        bill += 3
    elif add_pepperoni == 'y':
        bill += 2
    elif extra_cheese == 'y':
        bill += 1

elif size == 'm' or size == 'l':
    if add_pepperoni == 'y' and extra_cheese == 'y':
        bill += 4
    elif add_pepperoni == 'y':
        bill += 3
    elif extra_cheese == 'y':
        bill += 1

print(f'Your final bill is: ${bill}.')
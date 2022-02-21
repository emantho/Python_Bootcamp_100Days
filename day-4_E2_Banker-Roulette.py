from os import system
import random
system("clear")


# 🚨 Don't change the code below 👇
#test_seed = int(input("Create a seed number: "))
#random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") # This function split the string into a list using ',' as separator
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# use len to know how many item the list has
list_lenght = len(names) #; print(list_lenght) 

# Generating integer among 0 and item numbers entered for user
random_list_items = random.randint(0 , list_lenght - 1) # -> Remember to erase one (1) item from total
#print(random_list_items)

# using ramdon number generated to call index from list
winner = names[random_list_items]
print(f"{winner} is going to buy the meal today!")







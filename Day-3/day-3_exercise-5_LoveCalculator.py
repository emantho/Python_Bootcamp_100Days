from os import system

system("clear")
# system("cls")

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
true = 0
love = 0

combined = name1 + name2

true += combined.count("t")
true += combined.count("r")
true += combined.count("u")
true += combined.count("e")

love += combined.count("l")
love += combined.count("o")
love += combined.count("v")
love += combined.count("e")

loveScore = int(str(true) + str(love))
if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")

elif 40 <= loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")

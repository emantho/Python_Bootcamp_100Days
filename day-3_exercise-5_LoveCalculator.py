from os import system
#system('clear')
system("cls")

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true = 0 
love = 0

if 't' in name1 or 'r' in name1 or 'u' in name1 or 'e' in name1 or 't' in name2 or 'r' in name2 or 'u' in name2 or 'e' in name2:
   
    true += name1.count("t")
    true += name2.count("t")
  
    true += name1.count("r")
    true += name2.count("r")
   
    true += name1.count("u")
    true += name2.count("u")
   
    true += name1.count("e")
    true += name2.count("e")
    

if 'l' in name1 or 'o' in name1 or 'v' in name1 or 'e' in name1 or 'l' in name2 or 'o' in name2 or 'v' in name2 or 'e' in name2:
    love += name1.count("l")
    love += name2.count("l")
   
    love += name1.count("o")
    love += name2.count("o")
    
    love += name1.count("v")
    love += name2.count("v")
    
    love += name1.count("e")
    love += name2.count("e")


loveScore = int(str(true) + str(love))
if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")

elif 40 <= loveScore <= 50:
    print(f"Your score is {loveScore}, you are already togeter.")
else:
    print(f"Your score is {loveScore}.")
   

#print(f"result is: true{true} y love{love} total{true + love}")
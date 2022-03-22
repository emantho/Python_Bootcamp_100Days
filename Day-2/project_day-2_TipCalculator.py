from os import system
system("clear")

# Build a Tip calculator

#1. Show a welcome message
print("Welcome to the tip calculator.")
#2. Ask for the total of the bill
total_bill = float(input("What was the total bill? $"))
#3. Ask for the percentage of tig to give
customer_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100 + 1
#4. Ask how many people will be splitted the bill
people = int(input("How many people to split the bill? "))
#5. Show how much each people have to pay ?
person_total = (total_bill * customer_tip / people)
# -> person_total = (total_bill * 1.12 / people) 
print(f"Each person should pay: ${person_total:.2f}") 
#printing decimals var = "{:.2f}".format(varToConvert)



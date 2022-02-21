from os import system
system("clear")

#Write your code below this row 👇
total = 0
total_1 = 0 

for num in range(1,101):
    if num % 2 == 0:
        total += num

print(total)

for num in range(2,101,2): # start in 2 to avoid use odd numbers
    #if num % 2 == 0:
    total_1 += num

print(total_1)

from os import system

system("clear")

num_char = str(len(input("What is your name? ")))
print("your name has " + num_char + " Characters")

# Type checking
print(type(str(len(input("What is your name? ")))))

# type convertions

a = 123  # integer
b = str(a)
c = float(a)
d = int(b)

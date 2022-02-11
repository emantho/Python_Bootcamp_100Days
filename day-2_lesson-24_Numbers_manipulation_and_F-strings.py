from os import system
system("clear")

print(round(8 / 3, 2))
print(round(2.66666, 2))
print(8 // 3)
result = 4 / 2
result /= 2
print(result)

# Maths operations short forms
result += 1 ;   print(f"the result of ' +=' result = result +  1 is {result}")
result -= 1 ;   print(f"the result of ' -=' result = result -  1 is {result}")
result *= 1 ;   print(f"the result of ' *=' result = result *  1 is {result}")
result /= 1 ;   print(f"the result of ' /=' result = result /  1 is {result}")
result //= 1;   print(f"the result of '//=' result = result // 1 is {result}")
result %= 1 ;   print(f"the result of ' %=' result = result %  1 is {result}")
result **= 1;   print(f"the result of '**=' result = result ** 1 is {result}")

# F string print
print(f"{result}")

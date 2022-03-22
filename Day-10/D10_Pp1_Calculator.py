from os import system; system("clear")


# Addition
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    if n2 > 0:
        return n1 / n2
    else:
        return f"Cannot divide by Zero"

operations = {
    "+" : add, 
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

# Program start
num1 = int(input("What is the first number?: "))

for operation in operations:
    print(f"{operation}",end=" ")

operation_choise = input("\nPick an operation from the line above: ")

num2 = int(input("What is the second number?: "))

operation_function = operations[operation_choise]
first_answer = operation_function(num1, num2)

print(f"{num1} {operation_choise} {num2} = {first_answer}")

# Continuing operations 
operation_choise = input("\nPick another operation: ")

num3 = int(input("What is the next number?: "))

operation_function = operations[operation_choise]
second_answer = operation_function(first_answer, num3)

print(f"{first_answer} {operation_choise} {num3} = {second_answer}")

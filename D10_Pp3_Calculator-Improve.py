from os import system; system("clear")
from D10_art import logo

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
    return n1 / n2
    
    

operations = {
    "+" : add, 
    "-" : substract,
    "*" : multiply,
    "/" : divide
}

def calculation():
    print(logo)
    # Program start
    num1 = float(input("What is the first number?: "))
    print()

    for operation in operations:
        print(f"{operation}",end=" ")

    # Loop through infinte calculation
    continue_calculation = "y"
    while continue_calculation == "y":
        operation_choise = input("\n\nPick an operation : ")

        num2 = float(input("\n\nWhat is the next number?: "))

        while num2 == 0 and operation_choise == "/":
            print(f"Cannot divide by Zero.")
            num2 = float(input("\n\nWhat is the next number?: "))
        
        operation_function = operations[operation_choise]
        answer = operation_function(num1, num2)

        print(f"{num1} {operation_choise} {num2} = {answer}")

        # Continuing operations 
        continue_calculation = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a clean calculation: ")
        if continue_calculation == "y":
            num1 = answer
        else:
            continue_calculation = "n"
            calculation()

calculation()
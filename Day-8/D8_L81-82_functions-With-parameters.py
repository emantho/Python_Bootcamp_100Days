from os import system

system("clear")

# Function with parameter
def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet("Eder")

# function with more than one input || ALSO CALLED Positional Argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is like in {location}")


greet_with("Diana", "Aracataca")

# function with more than one input || ALSO CALLED Keyword Argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is like in {location}")


greet_with(name="Emilia", location="Santa Marta")

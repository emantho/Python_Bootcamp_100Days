dictionaries_structure = {"key": "value"}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary.
print(programming_dictionary["Bug"])

# Adding new item to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# Create an empty dictionary. | this method works also to wipe a dictionary
empty_dictionary = {}
print(empty_dictionary)

# Edit an item in a dictionary
programming_dictionary["Loop"] = "A moth in your computer"
print(programming_dictionary)

# Loopt through a dictionry
for thing in programming_dictionary:
    print(f"This form prints only {thing}")
print(f"This form prints {programming_dictionary.keys()}")
print(f"This form prints {programming_dictionary.values()}")
print(f"This form prints {programming_dictionary.items()}")

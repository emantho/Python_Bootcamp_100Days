
# Defining global scope variable
im_global_variable = "global"
"""
Can be accessed and modified from any part of the code
"""

# Definig local scope variable
def my_function():
    im_local_variable = "local"
    print(im_local_variable)
"""
Can be accessed and modified only from inside the function
"""

# Definig global scope variable inside a function
def my_function2():
    global im_global_variable 
    im_global_variable = "now in inside function2"
    print(im_global_variable)
"""
Can be accessed and modified only from inside the function
"""

# Defining global constants
PI = 3.14156
"""
Is a great idea name it using capital so when are caller you know those are global 
"""

# Calling global
print(im_global_variable) #>> OK

my_function()

# Calling local
# print(im_local_variable) #>> Error 

my_function2()


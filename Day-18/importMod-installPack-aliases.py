# IMPORTIN MODULES

# Using import and using its modules
import turtle

emi = turtle.Turtle()  # it require to use turtle.*

# Using from import
from turtle import Turtle

nana = Turtle()  # Less code to write


# MODULES ALIASES
import turtle as t

ed = t.Turtle()


# INSTALLING MODULES

import heroes  # before use this must be installed

# pip install heroes

print(heroes.gen())

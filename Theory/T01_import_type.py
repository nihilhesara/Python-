# Method 1 
import turtle
tim = turtle.Turtle()
tom = turtle.Turtle()

# Method 2 (most suitable way)
from turtle import Turtle
tim = Turtle()
tom = Turtle()

# Method 3 (doesn't use much becouse readability problems)
from turtle import *

# Method 4 (good method)
import turtle as t 
tim = t.Turtle()
tom = t.Turtle()

# pip install package_name (to install a package that isn't in the python library)
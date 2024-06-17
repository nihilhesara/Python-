import turtle as t 
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0,90,180,270]

for i in range(300):
    tim.color(random_color())                   # Radomly pick a colour 
    tim.pensize(10)                             # Thickness of the line
    tim.forward(30)
    tim.setheading(random.choice(directions))   # Randomly choose a random direction
    tim.speed("fastest")                        # Speed of the line (slowest,slow,normal,fast)
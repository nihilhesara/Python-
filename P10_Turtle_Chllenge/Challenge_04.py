import turtle as t 
import random

tim = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0,90,180,270]

for i in range(300):
    tim.color(random.choice(colours))           # Radomly pick a colour form the above list
    tim.forward(30)
    tim.setheading(random.choice(directions))   # Randomly choose a random direction
    tim.pensize(10)                             # Thickness of the line
    tim.speed("fastest")                        # Speed of the line
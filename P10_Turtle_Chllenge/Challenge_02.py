from turtle import Turtle, Screen

doted_line = Turtle()

# Penup and pendown for a dotted line
for i  in range(15):
    doted_line.forward(10)
    doted_line.penup()
    doted_line.forward(10)
    doted_line.pendown()

screen = Screen()
screen.exitonclick()
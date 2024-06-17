from turtle import Turtle, Screen

timmmy_the_turtle = Turtle()    # Give a variable 

for i in range(4):
    timmmy_the_turtle.forward(100)
    timmmy_the_turtle.left(90)      # 90 degree turn left

screen = Screen()   # To display the screen
screen.exitonclick()    # To exit the screen on a click
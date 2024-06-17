from turtle import Turtle, Screen 

tim = Turtle()

for i in range (36):
    tim.circle(100)
    tim.left(10)
    tim.speed(12)

screen = Screen()
screen.exitonclick()
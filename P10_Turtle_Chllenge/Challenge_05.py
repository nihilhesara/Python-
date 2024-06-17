from turtle import Turtle, Screen 

tim = Turtle()

for i in range (36):    # 36 circles 10 degree lef in all time so 360/10 = 36 
    tim.circle(100)     # circle radius 100 
    tim.left(10)
    tim.speed(10)

screen = Screen()
screen.exitonclick()
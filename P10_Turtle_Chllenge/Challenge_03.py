from turtle import Turtle, Screen 

shape = Turtle()

# Triangle
for i in range(3):
    shape.color("red")
    shape.forward(100)
    shape.right(120)    # angle (360/No of sides)
    
# Square
for j in range(4):
    shape.color("blue")
    shape.forward(100)
    shape.right(90)
    
# Pentagon
for k in range(5):
    shape.color("green")
    shape.forward(100)
    shape.right(72)
    
# Hexagon
for l in range(6):
    shape.color("brown")
    shape.forward(100)
    shape.right(60)

# Octagon
for m in range(8):
    shape.color("orange")
    shape.forward(100)
    shape.right(45)

# Decagon 
for k in range(10):
    shape.color("purple")
    shape.forward(100)
    shape.right(36)

'''colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)'''

screen = Screen()
screen.exitonclick()

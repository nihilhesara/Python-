from turtle import Turtle
import colorgram
# Install colorgram - pip install colorgram.py

rgb_colors = []
colors = colorgram.extract('C:\\Users\\ASUS\\Desktop\\Udemy Python\\Projects\\Python-\\image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(colors)
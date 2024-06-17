from turtle import Turtle
import colorgram
# Install colorgram - pip install colorgram.py

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 6)

print(colors)
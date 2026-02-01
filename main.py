from turtle import Turtle as t, Screen
import random

import polygon

tim = t()


tim.shape("turtle")
tim.color("red")
tim.color("LightSalmon4")

# Draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Drawing different shapes
# for _ in range(3):
#     tim.forward(100)
#     tim.right(120)
#
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# for i in range(5):
#     tim.forward(100)
#     tim.right(72)
colors = ["red", "green", "purple", "yellow", "pink","LightSalmon4", "SlateGrey","SeaGreen","CornflowerBlue"]

def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

# shapes = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()

# import heroes
# print(heroes.gen())



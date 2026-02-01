import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.pensize(10)
tim.speed("fastest")
# colours = ["CornflowerBlue", "SpringGreen", "RosyBrown", "wheat", "RoyalBlue", "OliveDrab", "firebrick", "SlateGray", "DarkOrchid"]
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))




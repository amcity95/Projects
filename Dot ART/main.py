import turtle
import colorgram
from turtle import Turtle
from turtle import Screen
import random


color = colorgram.extract("gg.jpg.webp", 10)
i = 0
rgb_bank = []
for _ in range(10):
    step_1 = color[i]
    step_2 = step_1.rgb
    rgb_bank.append(step_2)
    i += 1


turtle.colormode(255)
bobo = Turtle()
bobo.penup()
bobo.setx(-350)
bobo.sety(-300)
bobo.penup()
x = -340
for i in range(35):
    x += 20
    bobo.sety(x)
    bobo.setx(-350)
    for n in range(35):
        bobo.fd(10)
        bobo.dot(10, random.choice(rgb_bank))
        bobo.fd(10)

screen = Screen()
screen.exitonclick()
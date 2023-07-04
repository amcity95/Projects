from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

turtles = [t3, t2, t1]
x_cor = [20, 0, 20]

for (s, t) in zip(x_cor, turtles):
    t.color("white")
    t.shape("square")
    t.penup()
    t.setx(s)


while True:
    for n in turtles:
        n.fd(20)
        time.sleep(2)



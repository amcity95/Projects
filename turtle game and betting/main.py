import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(800, 800)

tim = Turtle()
tom = Turtle()
jon = Turtle()
snow = Turtle()
bran = Turtle()
ned = Turtle()


def turtle_on_go(name, y, color):
    name.shape("turtle")
    name.color(color)
    name.penup()
    name.setx(-380)
    name.sety(y)


names = [tim, tom, jon, snow, bran, ned]
color = ["red", "orange", "green", "cyan", "black", "gray"]
y_cooe = [350, 210, 70, -70, -210, -350]

for (n, c, y) in zip(names, color, y_cooe):
    turtle_on_go(name=n, y=y, color=c)
bet = screen.textinput("Race!", "What color to bet on?")
while True:
    tim.fd(randint(1, 30))
    tom.fd(randint(1, 30))
    jon.fd(randint(1, 30))
    snow.fd(randint(1, 30))
    bran.fd(randint(1, 30))
    ned.fd(randint(1, 30))

    if tim.xcor() >= 380:
        if bet == "red":
            print("Nice! red won.")
            break
        else:
            print("You lose! its red")
            break
    elif tom.xcor() > 380:
        if bet == "orange":
            print("NIce! it was orange.")
            break
        else:
            print("YOU LOSE! it was orange.")
            break
    elif jon.xcor() > 380:
        if bet == "green":
            print("Nice! it was green.")
            break
        else:
            print("You lose! it was green")
            break
    elif snow.xcor() > 380:
        if bet == "cyan":
            print("Nice! winter has com.")
            break
        else:
            print("You lose! it was cyan.")
            break
    elif bran.xcor() > 380:
        if bet == "black":
            print("Nice! it was bran the broken.")
            break
        else:
            print("YOU LOSE IT WAS bran the broken.")
            break
    elif ned.xcor() > 380:
        if bet == "gray":
            print("Nice! it was eddard.")
            break
        else:
            print("You los! it was gray aka eddard.")
            break

screen.exitonclick()

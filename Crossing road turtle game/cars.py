# Importing elements
from turtle import Turtle, Screen
from player import Player

# I made here the total car coordinates (x,y)
K = 1
L = [i for i in range(280, -280, -56)]
CARS_X = []
TOTAL_CARS = []
for X in range(-280, 280, 10):
    if K < 4 or 11 > K > 7 or 18 > K > 14 or 25 > K > 21 or 32 > K > 28 or 39 > K > 35 or 46 > K > 42 or 53 > K > 49:
        CARS_X.append(X)
        K += 1
    else:
        K += 1
for x in CARS_X:
    for y in L:
        cor = (x, y)
        TOTAL_CARS.append(cor)
# Here I split the two sequences of tuples to make it easier for making two lanes opposite direction
CARS_HEAD_1 = []
CARS_HEAD_2 = []
for _ in TOTAL_CARS:
    if K % 2 == 0:
        CARS_HEAD_1.append(_)
        K += 1
    elif K % 2 != 0:
        CARS_HEAD_2.append(_)
        K += 1


# making class of cars
class Cars(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.line_1 = []
        self.line_2 = []
        self.cars_making_1()
        self.cars_making_2()

    # here i make two seperated lines then initialize them, i did it in purpose for changing the seth
    def cars_making_1(self):
        for _ in CARS_HEAD_1:
            cpu = Turtle()
            cpu.shape("square")
            cpu.shapesize(0.5, 0.5)
            cpu.penup()
            cpu.color("white")
            cpu.goto(_)
            self.line_1.append(cpu)

    def cars_making_2(self):
        for _ in CARS_HEAD_2:
            cpu = Turtle()
            cpu.shape("square")
            cpu.shapesize(0.5, 0.5)
            cpu.penup()
            cpu.seth(180)
            cpu.color("white")
            cpu.goto(_)
            self.line_2.append(cpu)

    def cars_moving(self):
        for (a, b) in zip(self.line_1, self.line_2):
            a.fd(20)
            b.fd(20)


screen = Screen()
screen.bgcolor("black")
screen.setup(600, 800)
test1212 = Cars()
test1212.cars_moving()
joueur = Player()
screen.exitonclick()

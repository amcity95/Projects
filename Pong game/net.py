from turtle import Turtle

y = range(280, -280, -10)
x = []
COR_NET = []

for i in y:
    x.append(0)
for (a, b) in zip(x, y):
    lim = (a, b)
    COR_NET.append(lim)

n = 4
for i in range(9):
    COR_NET.pop(n)
    n += 5


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.net = []
        self.net_making()

    def net_making(self):
        for j in COR_NET:
            fillet = Turtle()
            fillet.shape("square")
            fillet.color("white")
            fillet.shapesize(0.5)
            fillet.penup()
            fillet.goto(j)
            self.net.append(fillet)

from turtle import Turtle

POSITIONS_SNAKES = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for n in POSITIONS_SNAKES:
            new = Turtle()
            new.shape("square")
            new.color("white")
            new.penup()
            new.goto(n)
            self.snakes.append(new)

    def game_on(self):
        for _ in range(len(self.snakes) - 1, 0, -1):
            self.snakes[_].goto(self.snakes[_ - 1].pos())
        self.snakes[0].fd(20)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].seth(0)

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].seth(90)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].seth(180)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].seth(270)

    def new_tale(self):
        new = Turtle()
        new.shape("square")
        new.penup()
        new.color("white")
        new.goto(self.snakes[-1].pos())
        self.snakes.append(new)

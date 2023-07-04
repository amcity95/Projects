# Importing elements for the project
from turtle import Screen, Turtle


# Making the screen adequate to the game
class Board:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(600, 800)
        self.screen.tracer(0)


# Making the scoreboard
class Score(Turtle):
    def __init__(self, s):
        Turtle.__init__(self)
        self.score = Turtle()
        self.score.color("white")
        self.score.penup()
        self.score.goto(0, 360)
        self.score.hideturtle()
        self.score.write(arg=f"Score: {s}", move=False, align="center", font=("Arial", 18, "normal"))

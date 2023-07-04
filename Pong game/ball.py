from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.shapesize()
        self.ball.color("white")
        self.ball.penup()
        self.ball_vx = 0
        self.ball_vy = 0

    def ball_moving(self):
        self.ball.setx(self.ball.xcor() + self.ball_vx)
        self.ball.sety(self.ball.ycor() + self.ball_vy)

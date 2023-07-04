from turtle import Turtle
POSITIONS_OF_SQUARES = [(-280, 20), (-280, 0), (-280, -20)]
POSITIONS_OF_CPU = [(280, 60), (280, 40), (280, 20)]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_squares = []
        self.cpu = []
        self.player1()
        self.player2()
        self.cpu_speed = 9

    def player1(self):
        for _ in POSITIONS_OF_SQUARES:
            new = Turtle()
            new.shape("square")
            new.color("white")
            new.penup()
            new.goto(_)
            self.paddle_squares.append(new)

    def player2(self):
        for _ in POSITIONS_OF_CPU:
            cpu = Turtle()
            cpu.shape("square")
            cpu.color("white")
            cpu.penup()
            cpu.goto(_)
            self.cpu.append(cpu)

    def cpu_moving_up(self):
        if self.cpu[0].ycor() != 280:
            for i in self.cpu:
                i.seth(90)
                i.fd(self.cpu_speed)

    def cpu_moving_down(self):
        if self.cpu[0].ycor() != 280:
            for i in self.cpu:
                i.seth(270)
                i.fd(self.cpu_speed)

    def moving_down(self):
        for i in self.paddle_squares:
            if self.paddle_squares[2].ycor() != -280:
                i.seth(270)
                i.fd(20)

    def moving_up(self):
        for i in self.paddle_squares:
            if self.paddle_squares[2].ycor() != 240:
                i.seth(90)
                i.fd(20)

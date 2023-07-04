from turtle import Screen
from padle import Paddle
from net import Net
from ball import Ball


screen = Screen()
screen.setup(600, 600)
screen.title("Pong game")
screen.bgcolor("black")
screen.tracer(0)
score = 0
player = Paddle()
fillet = Net()
boule = Ball()
screen.onkey(key="s", fun=player.moving_down)
screen.onkey(key="z", fun=player.moving_up)
screen.listen()


boule.ball_vx = 5
boule.ball_vy = 2
while True:
    screen.update()
    while True:
        boule.ball_moving()
        if player.cpu[0].distance(280, 280) > 9:
            screen.update()
            if boule.ball.ycor() > 275:
                boule.ball_vy *= -1
            elif boule.ball.ycor() < -275:
                boule.ball_vy *= -1
            elif boule.ball.distance(player.cpu[0]) < 20 or boule.ball.distance(player.cpu[1]) < 20 or boule.ball.distance(player.cpu[2]) < 20:
                boule.ball_vx *= -1
            elif boule.ball.distance(player.paddle_squares[0]) < 20 or boule.ball.distance(player.paddle_squares[1]) < 20 or boule.ball.distance(player.paddle_squares[2]) < 20:
                boule.ball_vx *= -1
            elif boule.ball.xcor() > 275:
                score += 1
                boule.ball_vx *= -1
            elif boule.ball.xcor() < -275:
                boule.ball_vx *= -1
            player.cpu_moving_up()
        else:
            break
    while True:
        boule.ball_moving()
        if player.cpu[0].distance(280, -280) > 49:
            screen.update()
            if boule.ball.ycor() > 275:
                boule.ball_vy *= -1
            elif boule.ball.ycor() < -275:
                boule.ball_vy *= -1
            elif boule.ball.distance(player.cpu[0]) < 20 or boule.ball.distance(player.cpu[1]) < 20 or boule.ball.distance(player.cpu[2]) < 20:
                boule.ball_vx *= -1
            elif boule.ball.distance(player.paddle_squares[0]) < 20 or boule.ball.distance(player.paddle_squares[1]) < 20 or boule.ball.distance(player.paddle_squares[2]) < 20:
                boule.ball_vx *= -1
            elif boule.ball.xcor() > 275:
                score += 1
                boule.ball_vx *= -1
            elif boule.ball.xcor() < -275:
                boule.ball_vx *= -1
            player.cpu_moving_down()
        else:
            break

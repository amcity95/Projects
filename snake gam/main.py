from snake import Snake
from turtle import Screen
import time
from food import Food

screen = Screen()
screen.setup(600, 600)
score = 0
screen.title("Score: 0")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.game_on()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.listen()
    if snake.snakes[0].distance(food) < 15:
        snake.new_tale()
        score += 1
        screen.title(f"Score: {score}")
        food.refresh()
    if snake.snakes[0].xcor() > 280 or snake.snakes[0].ycor() > 280 or snake.snakes[0].ycor() < -280 or snake.snakes[0].xcor() < -290:
        you_lose = screen.textinput("YOU LOSE!", "Tray Again?(y/n):")
        if you_lose == "y":
            continue
        elif you_lose == "n":
            break
        else:
            break

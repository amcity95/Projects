# importing screen and the Objects necessary for the game:
from turtle import Screen
from player import Player
from board import Board, Score

# Window
screen = Board()
# Score board
s = 0
score = Score(s)
# Player
player = Player()

screen.screen.update()
screen.screen.exitonclick()



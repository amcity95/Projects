# Importing Turtle class
from turtle import Turtle

# General data than can be used in encapsulation of the class
PLAYER_COOR = (0, -350)


# Making the player

class Player(Turtle):
    def __init__(self):
        # Inherit attributes and methods from Turtle class
        Turtle.__init__(self)
        # Making an attribute that will be assigned to the main player
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.color("white")
        self.player.penup()
        self.player.seth(90)
        self.player.goto(PLAYER_COOR)

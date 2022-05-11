# Turtle Graphics Game – Space Turtle Chomp

import tkinter as TK
import turtle

# Set up screen
turtle.setup(650, 650)
wn = turtle.Screen()
wn.bgcolor('navy')

# Create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
# penup() you don’t draw, pendown() you do draw
player.penup()

# Set speed variable
speed = 1


# While loops run 'while' a condition is true...
while True:
    player.forward(speed)



# Errors
    # - ModuleNotFoundError: No module named 'tkinter'
        # - 
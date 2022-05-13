# Turtle Graphics Game – Space Turtle Chomp
# This file contains all our initializations for the space turtle game

# Python Style Guide
# https://peps.python.org/pep-0008/#introduction

# Python Docs
# https://docs.python.org/3.6/contents.html

# Python Recommendations
# https://peps.python.org/pep-0008/#programming-recommendations

import turtle
import random


SCREEN_WIDTH = 650
SCREEN_HEIGHT = 650
BOUNDARY_MIN = -290
BOUNDARY_MAX = 290

# Set up screen
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn = turtle.Screen()
wn.bgcolor('navy')


# Set window border
MY_PEN = turtle.Turtle()
MY_PEN.penup()
MY_PEN.setposition(-300,-300)
MY_PEN.pendown()
MY_PEN.pensize(3)
MY_PEN.color('white')
for side in range(4):
    MY_PEN.forward(600)
    MY_PEN.left(90)
MY_PEN.hideturtle()


# Create player turtle
PLAYER = turtle.Turtle()
PLAYER.color('darkorange')
PLAYER.shape('turtle')
# penup() stops drawing on screen, pendown() draws on screen
PLAYER.penup()
# 0 is the fastest animation speed.
PLAYER.speed(0)


# Initialize speed
# This is not written in the naming convention of a constant as we intend to update this variable.
speed = 1


# Create food
FOOD = turtle.Turtle()
FOOD.color("lightgreen")
FOOD.shape("circle")
FOOD.penup()
FOOD.speed(0)
FOOD.setposition(random.randint(BOUNDARY_MIN, BOUNDARY_MAX), random.randint(BOUNDARY_MIN, BOUNDARY_MAX))

# Turtle Graphics Game – Space Turtle Chomp

# Python Style Guide
# https://peps.python.org/pep-0008/#introduction

# Python Docs
# https://docs.python.org/3.6/contents.html

# Python Recommendations
# https://peps.python.org/pep-0008/#programming-recommendations

# Import all initializations from constants file
from ast import operator
from constants import *
import math
import random

def turn_left():
    PLAYER.left(30)

def turn_right():
    PLAYER.right(30)

def increase_speed():
    # To MODIFY a global variable from inside a function, we must use the 'global' keyword
    # However, we can call the global variable without stating the keyword. eg. print(speed)
    global speed
    speed += 1

def decrease_speed():
    # To MODIFY a global variable from inside a function, we must use the 'global' keyword
    # However, we can call the global variable without stating the keyword. eg. print(speed)
    global speed
    if speed == 1:
        return
    speed -= 1

def is_collision(t1, t2):
    # Collision checking between turtle and cabbage
    # Pythagorean theorem -> c^2 = a^2 + b^2
    d = math.sqrt(
        # return a value raised to the power of 2
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)
    )
    # if d < 20:
    #     return True
    # else:
    #     return False
    return True if d < 20 else False



def is_at_x_boundary(object):
    # if object.xcor() > BOUNDARY_MAX or object.xcor() < BOUNDARY_MIN:
    #     return True
    # else:
    #     return False

    # Ternary operator alternative
    return True if (object.xcor() > BOUNDARY_MAX or object.xcor() < BOUNDARY_MIN) else False

def is_at_y_boundary(object):
    # if object.ycor() > BOUNDARY_MAX or object.ycor() < BOUNDARY_MIN:
    #     return True
    # else:
    #     return False

    # Ternary operator alternative
    return True if (object.ycor() > BOUNDARY_MAX or object.ycor() < BOUNDARY_MIN) else False


# Set keyboard binding and listen for events
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(decrease_speed, 'Down')


# While loops run 'while' a condition is true...
# This will run our game infinitely
while True:
    PLAYER.forward(speed)

    # Boundary Player Checking x coordinate
    # if PLAYER.xcor() > 290 or PLAYER.xcor() < -290:
    #     PLAYER.right(180)

    # Boundary Player Checking y coordinate
    # if PLAYER.ycor() > 290 or PLAYER.ycor() < -290:
    #     PLAYER.right(180)


    # Boundary Food Checking x coordinate
    # if FOOD.xcor() > 290 or FOOD.xcor() < -290:
    #     FOOD.right(180)

    # Boundary Food Checking y coordinate
    # if FOOD.ycor() > 290 or FOOD.ycor() < -290:
    #     FOOD.right(180) 

    if is_at_x_boundary(PLAYER): PLAYER.right(180)
    if is_at_y_boundary(PLAYER): PLAYER.right(180)
    if is_at_x_boundary(FOOD): FOOD.right(180)
    if is_at_y_boundary(FOOD): FOOD.right(180)

    # Move food around
    FOOD.forward(3)

    # Collision checking
    if is_collision(PLAYER, FOOD):
        FOOD.setposition(
            random.randint(BOUNDARY_MIN, BOUNDARY_MAX),
            random.randint(BOUNDARY_MIN, BOUNDARY_MAX)
        )
        FOOD.right(random.randint(0, 360))


# Functions and Turtle
# Author: Katrina Chan
# Date: November 28, 2023

import turtle


burt = turtle.Turtle()

burt.color("lightblue")

def squared(num: float) -> float:
    """Takes a number and squares it."""

    return num ** 2

def draw_square(sidelength: int) -> None:
    """Draw a square of a given length."""

    burt.forward(sidelength)
    burt.left(90)
    burt.forward(sidelength)
    burt.left(90)
    burt.forward(sidelength)
    burt.left(90)
    burt.forward(sidelength)
    burt.left(90)

burt.speed(0)

# Draw squares that gro exponentially
for i in range(40):
    draw_square(squared(i))

turtle.done()
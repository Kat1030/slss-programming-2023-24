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

def draw_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree with initial given height in pixels
    
    Params:

    level - number representing the levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        # 1. Move turtle forward height pixels
        burt.forward(height)

        # 2. Turn turtle left 
        burt.left(36)
            # a. Draw a smaller tree to the left (current level - 1)
        draw_tree(level - 1, height * 0.75)

        # 3. Turn the turtle right
        burt.right(36 * 2)
            # a. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height * 0.75)

        # 4. Return to beginning
        burt.left(36)
        burt.back(height)

    else:
        original_colour = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_colour[0]) # revert to original colour

# Set-up Burt to draw trees
burt.color("brown")
burt.setheading(90) # points burt north
burt.width(4)       # trunk and branches thicker
burt.speed(5)

draw_tree(2, 175)

turtle.done()
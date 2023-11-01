# Pumpkin Drawing
# Author: Katrina Chan
# Date: 31 October 2023

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(0, 0)
carver.dot(10)
carver.forward(15)

# Left Eye
carver.setpos(-30, 20)
carver.dot(30)

# Right Eye
carver.penup()
carver.setpos(30, 20)
carver.dot(30)

# Mouth
carver.penup()
carver.setpos(-50, -30)
carver.dot(20)
carver.pendown()
carver.pensize(20)
carver.forward(100)

# Middle Sprout
carver.penup()
carver.setpos(0, 100)
carver.color("green")
carver.dot(20)
carver.pensize(20)
carver.pendown()
carver.setpos(0, 130)

# Left Sprout
carver.penup()
carver.setpos(0, 100)
carver.dot(20)
carver.pensize(20)
carver.pendown()
carver.setpos(-40, 120)

# Right Sprout
carver.penup()
carver.setpos(0, 100)
carver.dot(20)
carver.pensize(20)
carver.pendown()
carver.setpos(40, 120)

turtle.done()








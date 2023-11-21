# Turtle Example
# Author: Katrina Chan
# Date: November 21, 2023

import turtle

# Create a turtle that can be moved around the screen

FORWARD_MAGNITUDE = 20
LEFT_MAGNITUDE = 90
RIGHT_MAGNITUDE = 90

# Make a turtle
michaelangelo = turtle.Turtle()

# Get some input from the user
print("""To give commands, type:
      F - to go forward
      L - to turn left
      R - to turn right""")

# Repeat the below forever, or until the user says stop
done = False

while not done:
    command = input("Where should I go?").strip(",.?!").lower()

    # Move the turtle based on that input
    # Stop if the user says stop
    if command in ["f", "forward"]:
        michaelangelo.forward(FORWARD_MAGNITUDE)
    elif command in ["l", "left"]:
        michaelangelo.left(LEFT_MAGNITUDE)
        michaelangelo.forward(FORWARD_MAGNITUDE)
    elif command in ["r", "right"]:
        michaelangelo.right(RIGHT_MAGNITUDE)
        michaelangelo.forward(FORWARD_MAGNITUDE)
    elif command == "stop":
        done = True
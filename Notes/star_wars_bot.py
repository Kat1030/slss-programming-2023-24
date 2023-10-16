# Star Wars Bot
# Author: Katrina Chan
# Date: October 16, 2023

import time

# Create a bot that decides whether the user is on the Light Side or Dark Side

# Introduce the bot to the user
print("Hello! I will decide whether you belong on the Light Side or the Dark Side!")
time.sleep(1)

# Ask them if their favourite colour is red or if they like capes
colour_red = input("First off, is your favourite colour red?")
like_capes = input("Great! Now, do you like capes?")

# If they say yes to either, they are on the Dark Side
# If they say no to both, they are on the Light Side
if colour_red.lower().strip(".,?!") == "yes" or like_capes.lower().strip(",.?!") == "yes":
    print("You are on...")
    time.sleep(1.5)
    print("the DARK SIDE!!!")
else:
    print("You are on...")
    time.sleep(1.5)
    print("the LIGHT SIDE!!!")
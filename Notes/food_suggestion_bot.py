# Food Suggestion Bot
# Author: Katrina Chan
# Date: October 6, 2023

# A bot that asks the user what their favourite food is.
# Based on that food, it will classify the type/genre/cuisine of the food
# Give a restaurant suggestion

import random
import time

# Introduce the bot to the user
# Ask the user what their favourite food is
print("Hello, I am here to suggest you a restaurant!")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, tell me what your favourite food is.")
time.sleep(1)

# Italian Cuisine
italian_food = ["pasta", "pizza", "canneloni", "tiramisu", "italian", "italian food"]
# If they answer with Italian food, suggest an Italian restaurant
if fave_food.lower().strip("!,.?") in italian_food:
    print("I see that you might like Italian food!")
    time.sleep(1)
    print("I suggest Broli Kitchen.")
    time.sleep(1)
    print("Here's their address:")
    print("186-8180 No 2 Rd, Richmond, BC V7C 5K1")
else:
    print("Sorry, I do not know what type of food that is.")
    time.sleep(1)
    print("Unfortunately, I cannot provide you a suggestion.")
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

# Chinese Cuisine
chinese_food = [" chinese", "chinese food", "fried rice", "chow mein", "pot stickers", "dumplings", "stir fry", "steamed buns", "mapo tofu", "egg drop soup", "wontons", "lo mein", "ginger beef", "sweet and sour chicken", "rice balls"]
# Fast Food
fast_food = ["hamburgers", "fries", "french fries", "burgers", "chicken wings", "chicken nuggets"]
# Italian Cuisine
italian_food = [ "italian", "italian food", "pasta", "pizza", "canneloni", "tiramisu","prosciutto", "spaghetti", "meatballs", "spaghetti and meatballs", "fettucine", "fettucine alfredo", "risotto", "braciole"]
# Japanese Cuisine
japanese_food = ["japanese", "japanese food", "takoyaki", "ramen", "tonkatsu", "sushi", "sashimi", "chicken karage", "bento box", "teryaki", "tempura", "gyozas", "yakitori", "onigiri", "donburi", "soba", "udon", "miso soup", "okonomiyaki", "yakisoba"]
# Korean Cuisine
korean_food = ["korean", "korean food", "bibimbap", "bulgogi", "kimchi", "hangover stew", "samgyeopsal", "jjajangmyeon", "tteokbokki", "kimbap", "japchae"]
# If they answer with any of the above, suggest a restaurant accordingly
if fave_food.lower().strip("!.,?") in chinese_food:
    print("I see you might like Chinese food!")
    time.sleep(1)
    print("I suggest Dynasty Lite.")
    time.sleep(1)
    print("Here's their address:")
    print("8111, 160 Ackroyd Rd #160, Richmond, BC V6X 3J9")
elif fave_food.lower().strip("!.?,") in fast_food:
    print("I see you might like fast food!")
    time.sleep(1)
    print("I suggest Five Guys.")
    time.sleep(1)
    print("Here's their address:")
    print("11666 Steveston Hwy #3070, Richmond, BC V7A 5J3")
elif fave_food.lower().strip("!,.?") in italian_food:
    print("I see that you might like Italian food!")
    time.sleep(1)
    print("I suggest Broli Kitchen.")
    time.sleep(1)
    print("Here's their address:")
    print("186-8180 No 2 Rd, Richmond, BC V7C 5K1")
elif fave_food.lower().strip("!,.?") in japanese_food:
    print("I see you might like Japanese food.")
    time.sleep(1)
    print("I suggest G-Men Ramen.")
    time.sleep(1)
    print("Here's their address.")
    print("3711 Bayview St, Richmond, BC V7E 3B6")
elif fave_food.lower().stript(".,!?") in korean_food:
    print("I see you might like Korean food!")
    time.sleep(1)
    print("I suggest DAAN Korean Cuisine.")
    time.sleep(1)
    print("Here's their address:")
    print("9040 Blundell Rd #125, Richmond, BC V6Y 2N6")
else:
    print("Sorry, I do not know what type of food that is.")
    time.sleep(1)
    print("Unfortunately, I cannot provide you a suggestion.")
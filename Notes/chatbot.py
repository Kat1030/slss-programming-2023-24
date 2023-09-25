# Chatbot
# Author: Katrina Chan
# Date: September 20, 2023

import random
import time

# Greet the user
print("Hello there!")
time.sleep(1.5)
print("I'm a crude Chatbot, here to talk to you.")
time.sleep(1.5)

# Get the user's name and store it in a variable
user_name = input("So, what's your name?")

# Respond with the user's name in a friendly way
print(f"It's good to meet you, {user_name}.")
time.sleep(1.5)

# Ask the user what their favourite food is
fave_food = input("What's your favourite food?")

# Make a comment about their food but NOT BE TERRIBLY REPETITIVE
# Create a list of possible responses
food_responses = [
    f"Oh. I've never had {fave_food} before.",
    f"Cool! I love {fave_food}, too!",
    "I've heard that's delicious.",
    "Mmmmmm. That sounds good."]

# Choose one of those responses randomly
random_food_response = random.choice(food_responses)

# Print out that chosen response
print(random_food_response)


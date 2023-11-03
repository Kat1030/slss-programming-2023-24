# World Traveller
# Author: Katrina Chan
# Date: November 3, 2023

# Greet the user
print("Hello! I am here to tell you how many continents you've been to!")

# Create a list of continents
continents = [
    "Have you been to Asia?",
    "Have you been to Africa?",
    "Have you been to Europe?",
    "Have you been to North America?",
    "Have you been to South America?",
    "Have you been to Australia/Oceania?",
    "Have you been to Antarctica?"
]

number_of_continents = 0

# Ask them which continents they have been to
for question in continents:
    print(question)
    user_response = input()

    # Store their response
    if user_response.lower().strip(",.?!") in ["yes", "yeah", "yea", "yep"]:
        number_of_continents += 1

# Tell the user how many continents they have travelled to
print(f"You have travelled to {number_of_continents} continent(s)!")
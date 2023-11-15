# Parental Bot
# Author: Katrina Chan
# Date: November 15, 2023

# Create a list of questions to ask
chores = [
    "Did you eat?",
    "Did you study?",
    "Did you do your laundry?",
    "Did you call grandma?"
]

completed_chores = 0

# Ask the questions to the user
for question in chores:
    print(question)

    user_response = input().strip(",.?!")

    if user_response == "yes":
        completed_chores += 1

# Answer based on the user's responses
if completed_chores <= 0:
    print("I'm coming over.")
elif completed_chores <= 2:
    print("Ok.")
elif completed_chores <= 4:
    print("Good!")
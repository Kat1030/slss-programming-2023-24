# Similar Hobbies
# Author: Katrina Chan
# Date: November 14, 2023

# Ask the user for their hobbies, seperated by spaces
print("Please enter hobbies, seperated by spaces.")

# Get person 1's interests
person_1_hobbies = input("Person 1: ").lower().strip(",.?!")

# Get person 2's interests
person_2_hobbies = input("Person 2: ").lower().strip(",.?!")

# Initialize the similarity score
sim_score = 0

# Sim score algo
for item in person_1_hobbies.split(" "):
    if item in person_2_hobbies.split(" "):
        sim_score += 1

# Print the results
print(f"You have {sim_score} hobbies in common!")
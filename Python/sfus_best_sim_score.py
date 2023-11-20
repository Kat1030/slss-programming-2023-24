# SFU's Best
# Author: Katrina Chan
# Date: November 10, 2023

# Load data from .csv file
# Read it in a meaningful way
# Link our similarity score algo to the data

# Open the file
with open("./sfu_data.csv") as f:
    
    # Read the first line of data
    f.readline()

# Create a profile for someone that shows their favourite places at SFU
profile = [
    "Bubble World",
    "Chef Hung",
    "Uncle Fatih's",
    "Guadalupe (MBC)",
    "Steve's Poke Bar"
]

# Initialize our top similarity score and their name
top_sim_score = 0
top_sim_name = ""

with open("./sfu_data.csv") as f:
    # Throw away the header
    header = f.readline()

# For every line of data in the file (string)
    for line in f:
        # Convert the line of data into a list
        current_likes = line.split(",")

        # Initialize the CURRENT similarity score
        # Store the current person's name
        current_sim_score = 0
        current_name = current_likes[1]

        # Sim score algo
        for item in profile:
            if item in current_likes:
                current_sim_score += 1

        # Print the current sim_score
        print(f"{current_name} - Score: {current_sim_score}")

        # If the current score > top sim score
        if current_sim_score > top_sim_score:
            # Update the top sim score and name
            top_sim_score = current_sim_score
            top_sim_name = current_name

print("TOP SIMILAR PERSON!")
print(f"{top_sim_name} - Score: {top_sim_score}")
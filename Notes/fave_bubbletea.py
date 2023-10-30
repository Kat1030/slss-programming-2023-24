# Bubble Tea Popularity Algorithm
# Author: Katrina Chan
# Date: October 27, 2023

# Ask 5 users what their favourite bubble tea place is
# Prints out a summary of the data

# ------ CONSTANTS

NUM_RESPONDANTS = 5

# ------

# Like Counters
coco_likes = 0          # Initialize the variable to 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0
other_likes = 0

for _ in range(NUM_RESPONDANTS):
    # Ask the user what their favourite bubble tea place is
    print("What's your favourite bubble tea store?")

    fave_place = input().lower().strip(",.?!")

    # Tally or counting algo
    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1    # Alternate to above
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "bubble queen":
        bubqueen_likes += 1
    else:
        other_likes += 1

# Repeat the code above 5 times

# Round to two decimal places
round(coco_likes, 2)
round(suntea_likes, 2)
round(chatime_likes, 2)
round(bubqueen_likes, 2)
round(other_likes, 2)

# Print out a summary
print(f"CoCo Likes: {coco_likes} ({coco_likes / NUM_RESPONDANTS * 100}%)")
print(f"SunTea Likes: {suntea_likes} ({suntea_likes / NUM_RESPONDANTS * 100}%)")
print(f"Chatime Likes: {chatime_likes} ({chatime_likes / NUM_RESPONDANTS * 100}%)")
print(f"Bubble Queen Likes: {bubqueen_likes} ({bubqueen_likes / NUM_RESPONDANTS * 100}%)")
print(f"Other: {other_likes} ({other_likes / NUM_RESPONDANTS * 100}%)")
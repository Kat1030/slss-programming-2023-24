# Olympic Judging
# Author: Katrina Chan
# Date: November 1, 2023

# ------ CONSTANTS

NUM_RESPONDANTS = 5

# ------

final_score = 0

# Ask the user to rate the performance
print("Rate the performance on a scale of 1 to 10.".lower().strip(",.?!"))
rating_1 = int(input())
final_score += rating_1

print("Rate the performance on a scale of 1 to 10.".lower().strip(",.?!"))
rating_2 = int(input())
final_score += rating_2

print("Rate the performance on a scale of 1 to 10.".lower().strip(",.?!"))
rating_3 = int(input())
final_score += rating_3

print("Rate the performance on a scale of 1 to 10.".lower().strip(",.?!"))
rating_4 = int(input())
final_score += rating_4

print("Rate the performance on a scale of 1 to 10.".lower().strip(",.?!"))
rating_5 = int(input())
final_score += rating_5

# Do some math
average_score = final_score / 5

# Present the results to the user
print(f"Judge 1: {rating_1}")
print(f"Judge 2: {rating_2}")
print(f"Judge 3: {rating_3}")
print(f"Judge 4: {rating_4}")
print(f"Judge 5: {rating_5}")
print(f"Your Olympic Score is {average_score:.1f}")
# Loop Practice
# Author: Katrina Chan
# Date: October 10, 2023

# Create a list
groceries = ["hot wheels", "lego", "ice cream", "video games"]

# Do something for each thing in the list
# Print it out in a pretty way
# e.g.
# print(f"* {groceries[0]}")
# print(f"  ---")
# print(f"* {groceries[1]}")
# print(f"  ---")
# print(f"* {groceries[3]}")

for item in groceries:
    print(f"* {item}")
    print("  ---")

# Using the method above, create the thing below
# *
# **
# ***
# ****
# *****

pyramid = ["*", "**", "***", "****", "*****", "******"]

for row in pyramid:
    print(f"{row}")


import time

# Create a New Years Countdown that's automated
# Count out every second
# Print out "Happy New Year!" instead of 0

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy New Year!"]

for number in countdown:
    print(f"{number}")
    time.sleep(1)

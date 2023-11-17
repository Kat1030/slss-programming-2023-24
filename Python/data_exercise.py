from pathlib import Path


# File Exercises
# Author:
#

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file.
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

    # Print the second line
    print(f.readline())

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.
with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.
with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        list = line.split(",")

        print(list)

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.
# Problem 1:
# Open the file and print the contents of the second line in the file.
with open("./data_example.csv", encoding="utf-8") as f:
    adobo_likes = 0
    for line in f:
        list = line.split(",")
        
        if list[1] == "Chicken Adobo":
            adobo_likes += 1
    print(adobo_likes)

# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".
with open("./data_example.csv", encoding="utf-8") as f:
    name_initial = 0
    for line in f:
        list = line.split(",")

        if line[0] == "A":
            name_initial += 1
    print(name_initial)

# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?
with open("./data_example.csv", encoding="utf-8") as f:
    town_guangzhou = 0
    for line in f:
        list = line.strip().split(",")

        if list[4] == "Guangzhou":
            town_guangzhou += 1
    print(town_guangzhou)

# Problem 7:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.


# Problem 8:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?
top_food = 0
top_name = ""

with open("./data_example.csv", encoding="utf-8") as f:
    current_food = 0

    for line in f:
        list = line.split(",")
        current_food = list[1]

        for item in list:
            if item in current_food:
                top_food += 1
    if current_food > top_food:
        top_food = current_food
    print(top_food)
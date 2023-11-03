# Semester Evaluator
# Author: Katrina Chan
# Date: November 3, 2023

# Greet the user
print("Hello! I am here to ask how your courses are this semester!")

questions = [
    "How is your A Block on a scale of 1 to 5?",
    "How is your B Block on a scale of 1 to 5?",
    "How is your C Block on a scale of 1 to 5?",
    "How is your D Block on a scale of 1 to 5?"
]

final_score = 0

# Ask them to rate their course from 1 to 5
for question in questions:
    print(question)

    rating = int(input().lower().strip(",.?!"))
    final_score += rating

# Do some math
average_score = final_score / len(questions)

# Present the user their results and add a response
if average_score in "0, 1":
    print(f"{average_score:.2f}? Ouch.")
elif average_score in " ":
    print(f"{average_score}? Not a bad semester.")
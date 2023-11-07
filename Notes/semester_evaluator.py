# Semester Evaluator
# Author: Katrina Chan
# Date: November 3, 2023

# Greet the user
number_of_courses = int(input("Hello! How many courses are you taking?"))

final_score = 0

# Ask them to rate their course from 1 to 5

for i in range(number_of_courses):
    rating = int(input(f"how would you rate course {i+1} out of 5? "))
    final_score += rating
        
average_score = final_score / number_of_courses

# Present the user their results and add a response
if average_score <= 1:
    print(f"{average_score:.1f}? Ouch.")
elif average_score < 3:
    print(f"{average_score:.1f}? Not a bad semester.")
elif average_score >= 3:
    print(f"{average_score:.1f}? Glad to hear that!")
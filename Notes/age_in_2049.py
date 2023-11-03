# Age In 2049
# Author: Katrina Chan
# Date: November 1, 2023

# Greet the user
print("Hello! I will tell you how old you will be in 2049.")

# Ask the user their age
    # Store their response
user_age = input("How old are you right now?")

# Do some math
older_age = 2049 - 2023 + int(user_age.lower().strip(",.!?"))

# Present the results to the user
print(f"You will be {older_age} in 2049.")
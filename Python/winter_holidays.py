# Winter Holidays
# Author: Katrina Chan
# Date: January 8, 2024

import random

# Requirements:
# - create a function called winter_function()
#   - takes one parameter - string
#   - returns a summary of an event from your holidays

# Please do not use ChatGPT or any other LLM

good = [
    "I got lots of stuffies for Christmas."
    "I went on a trip with my family."
    "I shopped for presents at Richmond Centre."
    "My friends came over to my house."
]

bad = [
    "I went to Grouse Mountain and it was very cold."
    "My mom forced me to do chores."
]

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24
    
    Params:
        good_or_bad - indicate what kind of event to summarize
    
    Returns:
        an event that happened during the holidays
        the event is selected randomly"""

    good_or_bad = input("Was your Winter Break good or bad?")

    if good_or_bad.lower().strip(",.?!") in "good":
        return random.choice[good]
    elif good_or_bad.lower().strip(".,?!") in "bad":
        return random.choice[bad]

print(winter_holiday)

def main() -> None:
    # Runs all the things we want to test in our .py file
    winter_holiday("good")
    winter_holiday("bad")

if __name__ == "__main__":
    main()
# McDoland's Price Calculator
# Author: Katrina Chan
# Date: November 3, 2023

# Greet the user
print("Hello, welcome to McDoland's!")

# Ask if they want a burger for $5 and fries for $3 with %14 tax

burger = input("Would you like a burger for $5?")
fries = input("Would you like fries for $3?")

order = 0

if burger.lower().strip(",.?!") in "yes":
    order += 5

if fries.lower().strip(",.?!") in "yes":
    order += 3

# Add tax
total_payment = (float(order) * 0.14) + float(order)

# Present the user their total
print(f"Your total for today is ${total_payment:.2f}! Thank you for stopping by McDoland's!")
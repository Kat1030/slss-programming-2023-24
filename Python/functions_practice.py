# Funtions Practice
# Author: Katrina Chan
# Date: November 23, 2023

def area_of_a_square(sidelength:float) -> float:
	"""Return the area of a square.
	Results are in units squared.
	
	Params:
	
	sidelength - length of one side of the square"""

	area = sidelength ** 2

	return area


def print_area_of_a_square(sidelength: float):
	"""Calculate and print the area of a square.
	Results are in units squared.
	
	Params:
	
	sidelength - length of one side of the square"""

	area = sidelength ** 2
	
	print(f"The area of a square with side length {sidelength} is: {area} square units.")

print_area_of_a_square(12.2)

# Given two sidelengths
    # 12.2 and 144
# Add the area of both squares

area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
print(area_of_squares)


# QUESTION 1

# Write a function called stars()
	# It takes int as a parameter

# Aside: Signature of a function
	# name of the function
	# inputs/parameters/type
	# return type
def stars(num_stars: int) -> str:
	"""Print the amount of stars from the argument.
	
	Params:
	
	num_stars - number of stars to return"""

	return "*" * num_stars

# Return the same number of stars as the argument
print(stars(2))


# QUESTION 2

# Write a function that takes three numbers called biggest_of_three()
	# It should return the biggest of the three numbers
def biggest_of_three(num_1: float, num_2: float, num_3: float) -> float:
	"""Take three numbers and return the largest of those three numbers.
	
	Params:
	
	num_1 - the first number
	num_2 - the second number
	num_3 - the third number
	biggest_num - the largest of the three numbers
	
	Returns:
	
	The biggest of the three numbers"""

	if num_1 > num_2 > num_3 or num_1 > num_3 > num_2:
		biggest_num = num_1
	elif num_2 > num_1 > num_3 or num_2 > num_3 > num_1:
		biggest_num = num_2
	elif num_3 > num_1 > num_2 or num_3 > num_2 > num_1:
		biggest_num = num_3

	return biggest_num

print(biggest_of_three(29, 56, 3))


# QUESTION 3

# Write a function that creates a pyramid of stars called pyramid()
def pyramid(num_rows: int) -> None:
	"""Print the amount of rows from the argument.
	
	Params:
	
	num_rows - the amount of rows of the pyramid"""

	for i in range(num_rows):
		print("*" * (i + 1))

	for current_layer in range(1, num_rows + 1):
		print(stars(current_layer))

	return num_rows

print(pyramid(9))


# QUESTION 4

# Write a function that creates a mirrored pyramid of stars called pyramid_mirror()
def pyramid_mirror(num_rows: int) -> str:
	"""Print a mirrored pyramid.
	
	Params:
	
	num_rows - the amount of rows of the pyramid"""

	for current_layer in range(1, num_rows + 1):
		# Print the spaces then print the stars
		# num_layers == 2
			# " " * 1  + stars(1)
			# " " * 0  + stars(2)
		print(" " * (num_rows - current_layer) + stars(current_layer))

	return num_rows

print(pyramid_mirror(7))
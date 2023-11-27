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
	"""Calculate and pring the area of a square.
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
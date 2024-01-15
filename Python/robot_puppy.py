# Robot Puppy
# Author: Katrina Chan
# Date: January 12, 2024

from PIL import Image

import colour_helper

# Create a python file that calculates the x, y location of the centre of the ball
    # You might want to try list append and the sum function

ball_image = Image.open("./Images/Red Ball.jpeg")
red_pixels = []
red_y_pixels = []
red_x_pixels = []
amount_of_pixels = 0
pixel_on_y = 0
pixel_on_x = 0


# Visit every pixel in the image
for y in range(ball_image.height):
    for x in range(ball_image.width):
        current_pixel = ball_image.getpixel((x, y))

        # If that pixel is red, store it's location
        if colour_helper.pixel_to_string(current_pixel) == "ball red":
            red_pixels.append((x, y))
            amount_of_pixels += 1

print(pixel_on_y)

ball_image.close()
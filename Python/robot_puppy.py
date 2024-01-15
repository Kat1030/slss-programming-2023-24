# Robot Puppy
# Author: Katrina Chan
# Date: January 12, 2024

from PIL import Image

import colour_helper

# Create a python file that calculates the x, y location of the centre of the ball
    # You might want to try list append and the sum function

ball_image = Image.open("./Images/Red Ball.jpeg")
red_pixels_x = []
red_pixels_y = []

# Visit every pixel in the image
for y in range(ball_image.height):
    for x in range(ball_image.width):
        current_pixel = ball_image.getpixel((x, y))

        # If that pixel is red, store it's location
        if colour_helper.pixel_to_string(current_pixel) == "ball red":
            red_pixels_x.append(x)
            red_pixels_y.append(y)

avg_x = sum(red_pixels_x) / len(red_pixels_x)
avg_y = sum(red_pixels_y) / len(red_pixels_y)

print(f"Centre of Red Ball: ({round(avg_x, 2)}, {round(avg_y, 2)})")

ball_image.close()


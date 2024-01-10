# Jelly Bean Colour Counter
# Author: Katrina Chan
# Date: January 9, 2024

# Version 0.1
# Count all red pixels
# Report on the percentage of all red

from PIL import Image

import colour_helper

RED_PIXEL = (150, 0, 0)

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")
red_pixels = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        current_pixel = jelly_bean_img.getpixel((x, y))

    # If that pixel is red, store the location
        if colour_helper.pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))
    

# Count every pixel in the list
# Divide that number by the total pixels in the image
red_percentage = len(red_pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100

# Create a map of all red pixels
# Create a new image that is the same size as the original
original_size = (jelly_bean_img.width, jelly_bean_img.height)
red_pixel_map = Image.new("RGB", original_size)

# For every red pixerl in red_pixels, place a red pixel on that new image
for pixel_loc in red_pixels:
    red_pixel_map.putpixel(pixel_loc, RED_PIXEL)

red_pixel_map.save("./Images/red_pixel_map.jpg")

red_pixel_map.close()
jelly_bean_img.close()

# Display report
print(f"Red Jelly Beans: {round(red_percentage, 2)}")
# Jelly Bean Colour Counter
# Author: Katrina Chan
# Date: January 9, 2024

# Version 0.1 ---
# Count all red pixels
# Report on the percentage of all red jelly beans
# Version 0.2 ---
# Count all the green pixels
# Report on the percentage of all green jelly beans
# Version 0.3 ---
# Count all the blue pixels
# Report on the percentage of all blue jelly beans
# Version 0.4 ---
# Count all the yellow pixels
# Report on the percentage of all yellow jelly beans
# Version 0.5 ---
# Count all the pink pixels
# Report on the percentage of all pink jelly beans

from PIL import Image

import colour_helper

RED_PIXEL = (150, 0, 0)
YELLOW_PIXEL = (250, 200, 0)
GREEN_PIXEL = (0, 150, 0)
BLUE_PIXEL = (0, 0, 150)
PINK_PIXEL = (200, 100, 150)

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")
red_pixels = []
yellow_pixels = []
green_pixels = []
blue_pixels = []
pink_pixels = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        current_pixel = jelly_bean_img.getpixel((x, y))

    # If that pixel is red, store the location
        if colour_helper.pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))
        elif colour_helper.pixel_to_string(current_pixel) == "yellow":
            yellow_pixels.append((x, y))
        elif colour_helper.pixel_to_string(current_pixel) == "jelly bean green":
            green_pixels.append((x, y))
        elif colour_helper.pixel_to_string(current_pixel) == "blue":
            blue_pixels.append((x, y))
        elif colour_helper.pixel_to_string(current_pixel) == "pink":
            pink_pixels.append((x, y))

# Calculate the percentage of all the jelly bean colours
red_percentage = len(red_pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100
yellow_percentage = len(yellow_pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100
green_percentage = len(green_pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100
blue_percentage = len(blue_pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100
pink_percentage = len(pink_pixels) / (jelly_bean_img.width * jelly_bean_img.height) * 100

# Create a map of all "found" pixels for a respective colour
# Create a new image that is the same size as the original
original_size = (jelly_bean_img.width, jelly_bean_img.height)
pixel_map = Image.new("RGB", original_size)

# For every red pixer location in "found" pixel list, place a red pixel on that new image
for pixel_loc in red_pixels:
    pixel_map.putpixel(pixel_loc, RED_PIXEL)
for pixel_loc in yellow_pixels:
    pixel_map.putpixel(pixel_loc, YELLOW_PIXEL)
for pixel_loc in green_pixels:
    pixel_map.putpixel(pixel_loc, GREEN_PIXEL)
for pixel_loc in blue_pixels:
    pixel_map.putpixel(pixel_loc, BLUE_PIXEL)
for pixel_loc in pink_pixels:
    pixel_map.putpixel(pixel_loc, PINK_PIXEL)

pixel_map.save("./Images/pixel_map.jpg")

pixel_map.close()
jelly_bean_img.close()

# Display report
print(f"Red Jelly Beans: {round(red_percentage, 2)}%")
print(f"Yellow Jelly Beans: {round(yellow_percentage, 2)}%")
print(f"Green Jelly Beans: {round(green_percentage, 2)}%")
print(f"Blue Jelly Beans: {round(blue_percentage, 2)}%")
print(f"Pink Jelly Beans: {round(pink_percentage, 2)}%")
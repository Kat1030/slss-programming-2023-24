# Images and Python
# Author: Katrina Chan
# Date: December 11, 2023

import colour_helper

from PIL import Image

# Recall that we can open up files in Python
with Image.open("./Images/kid-green.jpg") as im:
    # Algorithm to visit every pixel in the kid-green image
    # Store the height and width of the image
    image_height = im.height
    image_width = im.width

    # Load the background image
    # ** remember to close it at the end
    bg_im = Image.open("./Images/beach.jpg")

    # Outer loop is top -> bottom
    # Inner loop is left -> right
    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))

            # check pixel to see if it's green
            if colour_helper.pixel_to_string(pixel) == "green":
                # If is is, replace it with bg_img pixel from the same coordinates
                bg_pixel = bg_im.getpixel((x, y))
                im.putpixel((x, y), bg_pixel)

    bg_im.close

    # save the image
    im.save("./Images/output.jpg")
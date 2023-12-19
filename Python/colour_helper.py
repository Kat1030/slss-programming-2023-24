# Colour Helper
# Author: Katrina Chan
# Date: December 13, 2023

# Do you help with colours?

# This is for you!

def pixel_to_string(pixel: tuple) -> str:
    """Take a rgb 3-tuple and "interpret it" as a colour and return that colour's name
    
    Params:
        pixel - 3-tuple of (red, green, blue)
        
    Return:
        String representing the colour"""
    
    r, g, b = pixel

    if g > 120 and r < 140 and b < 150:
        return "green"


from PIL import Image

# Write a function 'is_light' that takes as a parameter a tupel names 'pixel'
    # Returns True if average tupel value >= 128
    # Returns False if average tupel value <= 128
def is_light(pixel: tuple) -> bool:
    """Returns true if given pixel is "light"

    Params:
        pixel - 3-tuple of values red, green, blue

    Returns:
        True if pixel is light false if not
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + green + blue) / 3

    if average >= 128:
        return True
    else:
        return False


# Recall that we can open up files in Python
with Image.open("./Images/best_pizza.jpg") as im:
    # Store the height and width of the image
    image_height = im.height
    image_width = im.width

    white_pixel = (255, 255, 255)
    black_pixel = (0, 0, 0)

    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))

            if is_light(pixel) == True:
                im.putpixel((x, y), white_pixel)
            elif is_light(pixel) == False:
                im.putpixel((x, y), black_pixel)

    im.save("./Images/result.jpg")
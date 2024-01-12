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
    if g < 25 and b < 25 and r > 150:
        return "red"
    if g > 150 and b < 25 and r > 200:
        return "yellow"
    if g >= 60 and b < 50 and r < 50:
        return "jelly bean green"
    if g < 90 and b > 90 and r < 90:
        return "blue"
    if g < 100 and b > 100 and r > 150:
        return "pink"
    if g < 100 and b < 100 and r > 150:
        return "ball red"


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


def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Returns a grayscale version of the given pixel"""
    gray = str(pixel[0] * 0.3 + pixel[1] * 0.59 + pixel[2] * 0.11)

    return (gray, gray, gray)
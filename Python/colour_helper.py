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
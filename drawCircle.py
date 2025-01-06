from defaultPixel import sendPixel
import math
from typing import List, Set, Tuple

def drawCircle(color: List[int], startx: int, starty: int, radius: int) -> None:
    """
    Draws a circle on a canvas starting from a specified center point.

    Parameters:
    - color (list): A list representing the RGB color of the circle, formatted as [R, G, B].
    - startx (int): The x-coordinate of the center of the circle.
    - starty (int): The y-coordinate of the center of the circle.
    - radius (int): The radius of the circle in pixels.
    """
	# before startinig check that it wont go outside canvas:
    if not (0 <= startx - radius < 200 and 0 <= startx + radius < 200 and
            0 <= starty - radius < 200 and 0 <= starty + radius < 200):
        raise ValueError("Circle exceeds canvas bounds.")

    # Set to store unique pixel coordinates
    drawn_pixels: Set[Tuple[int, int]] = set()

    # Draw the circle using parametric equations
    for angle in range(360):
        radian = math.radians(angle)
        x = int(startx + radius * math.cos(radian))
        y = int(starty + radius * math.sin(radian))

        # Ensure the coordinates are within the canvas bounds
        if 0 <= x < 200 and 0 <= y < 200:
            # Add the pixel to the set if it's not already drawn
            if (x, y) not in drawn_pixels:
                drawn_pixels.add((x, y))
                pixel = {'x': x, 'y': y, 'color': color}
                sendPixel(pixel)
                
"""
The `drawCircle` function uses trigonometric functions to calculate the x and y coordinates of a circle's perimeter. Here's how the angle affects the coordinates:

1. **Angle 0° to 90° (First Quadrant)**:
   - **Cosine (cos)**: Positive, causing x to increase.
   - **Sine (sin)**: Positive, causing y to increase.
   - The circle is drawn in the top-right corner relative to the center.

2. **Angle 90° to 180° (Second Quadrant)**:
   - **Cosine (cos)**: Negative, causing x to decrease.
   - **Sine (sin)**: Positive, causing y to increase.
   - The circle is drawn in the top-left corner relative to the center.

3. **Angle 180° to 270° (Third Quadrant)**:
   - **Cosine (cos)**: Negative, causing x to decrease.
   - **Sine (sin)**: Negative, causing y to decrease.
   - The circle is drawn in the bottom-left corner relative to the center.

4. **Angle 270° to 360° (Fourth Quadrant)**:
   - **Cosine (cos)**: Positive, causing x to increase.
   - **Sine (sin)**: Negative, causing y to decrease.
   - The circle is drawn in the bottom-right corner relative to the center.

--- the use of Set[] ---   
The function uses a set to store unique pixel coordinates.
This ensures that each pixel is only sent once, avoiding duplicates and optimizing the drawing process. 
The set provides efficient lookups to check if a pixel has already been drawn, 
maintaining uniqueness and improving performance.   

By iterating through these angles, the function calculates the perimeter of the circle and sends each unique pixel to the server.
"""

def drawCircleFill(color: List[int], startx: int, starty: int, radius: int) -> None:
    # check if its in bounds
    if not (0 <= startx - radius < 200 and 0 <= startx + radius < 200 and
            0 <= starty - radius < 200 and 0 <= starty + radius < 200):
        raise ValueError("Circle exceeds canvas bounds.")
    # call drawCircle from the Maths library
    for rad in range(radius, -1, 0):
        drawCircle(color, startx, starty, rad)
    # write surrounding pixel of 1 since they are inefficient to calc with math library
    surrounding_pixels = [
        (startx + 1, starty), (startx - 1, starty),  # Right and Left
        (startx, starty + 1), (startx, starty - 1),  # Down and Up
        (startx + 1, starty + 1), (startx - 1, starty - 1),  # Diagonal Down-Right and Up-Left
        (startx + 1, starty - 1), (startx - 1, starty + 1)   # Diagonal Up-Right and Down-Left
    ]
    for x, y in surrounding_pixels:
            pixel = {'x': x, 'y': y, 'color': color}
            sendPixel(pixel)
	# send center pixel
    pixel = {'x': startx, 'y': starty, 'color': color}
    sendPixel(pixel)
    
     
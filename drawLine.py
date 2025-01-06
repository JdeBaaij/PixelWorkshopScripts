from defaultPixel import sendPixel
from typing import List

# This function, drawLine, draws a line on a canvas using a specified color and starting point.
# The color parameter should be in the format [R, G, B], where R, G, and B are integers representing the red, green, and blue color components.
# The startx and starty parameters define the starting coordinates of the line on the canvas.
# The direction parameter specifies the direction of the line: 'u' for up, 'd' for down, 'r' for right, and 'l' for left.
# length determines the amount of pixels drawn
def drawLine(color: List[int], startx: int, starty: int, direction: str, length: int) -> None:
    """
    Draws a straight line on a canvas starting from a specified point.

    Parameters:
    - color (list): A list representing the RGB color of the line, formatted as [R, G, B].
    - startx (int): The x-coordinate of the starting point of the line.
    - starty (int): The y-coordinate of the starting point of the line.
    - direction (str): The direction of the line. Valid options are 'u' (up), 'd' (down), 'r' (right), and 'l' (left).
    - length (int): The number of pixels the line should be drawn.

    Raises:
    - ValueError: If the direction is not one of 'u', 'd', 'r', or 'l'.
    """
    # Draw the line based on the direction and length
    for step in range(length):
        if direction == 'u':  # Up
            y = starty - step
            x = startx
        elif direction == 'd':  # Down
            y = starty + step
            x = startx
        elif direction == 'r':  # Right
            x = startx + step
            y = starty
        elif direction == 'l':  # Left
            x = startx - step
            y = starty
        else:
            raise ValueError("Invalid direction. Use 'u', 'd', 'r', or 'l'.")

        # Ensure the coordinates are within the canvas bounds
        if not (0 <= x < 200 and 0 <= y < 200):
            break  # Exit the loop if x or y is out of bounds

        # Create a pixel for each coordinate
        pixel = {'x': x, 'y': y, 'color': color}
        # Send the pixel to the server
        sendPixel(pixel)


def drawDiagonalLine(color: List[int], startx: int, starty: int, direction: str, length: int) -> None:
    """
    Draws a diagonal line on a canvas starting from a specified point.

    Parameters:
    - color (list): A list representing the RGB color of the line, formatted as [R, G, B].
    - startx (int): The x-coordinate of the starting point of the line.
    - starty (int): The y-coordinate of the starting point of the line.
    - direction (str): The direction of the line. Valid options are 'ur', 'dr', 'ul', and 'dl'.
    - length (int): The number of pixels the line should be drawn.

    Raises:
    - ValueError: If the direction is not one of 'ur', 'dr', 'ul', or 'dl'.
    """
    # Draw the diagonal line based on the direction and length
    for step in range(length):
        if direction == 'ur':  # Up-Right
            x = startx + step
            y = starty - step
        elif direction == 'dr':  # Down-Right
            x = startx + step
            y = starty + step
        elif direction == 'ul':  # Up-Left
            x = startx - step
            y = starty - step
        elif direction == 'dl':  # Down-Left
            x = startx - step
            y = starty + step
        else:
            raise ValueError("Invalid direction. Use 'ur', 'dr', 'ul', or 'dl'.")

        # Ensure the coordinates are within the canvas bounds
        if not (0 <= x < 200 and 0 <= y < 200):
            break

        # Create a pixel for each coordinate
        pixel = {'x': x, 'y': y, 'color': color}
        # Send the pixel to the server
        sendPixel(pixel)
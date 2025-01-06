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
    if direction == 'u':  # Up
        xstep, ystep = 0, -1
    elif direction == 'd':  # Down
        xstep, ystep = 0, 1
    elif direction == 'r':  # Right
        xstep, ystep = 1, 0
    elif direction == 'l':  # Left
        xstep, ystep = -1, 0
    else:
        raise ValueError("Invalid direction. Use 'u', 'd', 'r', or 'l'.")



    for step in range(length):
        x = startx + step * xstep
        y = starty + step * ystep
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
    if direction == 'ur':  # Up-Right
        xstep, ystep = 1, -1
    elif direction == 'dr':  # Down-Right
        xstep, ystep = 1, 1
    elif direction == 'ul':  # Up-Left
        xstep, ystep = -1, -1
    elif direction == 'dl':  # Down-Left
        xstep, ystep = -1, 1
    else:
        raise ValueError("Invalid direction. Use 'ur', 'dr', 'ul', or 'dl'.")

    # Draw the diagonal line based on the direction and length
    for step in range(length):
        x = startx + step * xstep
        y = starty + step * ystep

        # Ensure the coordinates are within the canvas bounds
        if not (0 <= x < 200 and 0 <= y < 200):
            break

        # Create a pixel for each coordinate
        pixel = {'x': x, 'y': y, 'color': color}
        # Send the pixel to the server
        sendPixel(pixel)


def drawSquare(color: List[int], startx: int, starty: int, side_length: int) -> None:
    """
    Draws a square on a canvas starting from a specified point.

    Parameters:
    - color (list): A list representing the RGB color of the square, formatted as [R, G, B].
    - startx (int): The x-coordinate of the top-left corner of the square.
    - starty (int): The y-coordinate of the top-left corner of the square.
    - side_length (int): The length of each side of the square.
    """
    # Draw the four sides of the square
    drawLine(color, startx, starty, 'r', side_length)  # Top side
    drawLine(color, startx, starty, 'd', side_length)  # Left side
    drawLine(color, startx + side_length - 1, starty, 'd', side_length)  # Right side
    drawLine(color, startx, starty + side_length - 1, 'r', side_length)  # Bottom side


def drawFilledSquare(color: List[int], startx: int, starty: int, side_length: int) -> None:
    """
    Draws a filled square on a canvas starting from a specified point.

    Parameters:
    - color (list): A list representing the RGB color of the square, formatted as [R, G, B].
    - startx (int): The x-coordinate of the top-left corner of the square.
    - starty (int): The y-coordinate of the top-left corner of the square.
    - side_length (int): The length of each side of the square.
    """
    # Draw horizontal lines to fill the square
    for y in range(starty, starty + side_length):
        drawLine(color, startx, y, 'r', side_length)
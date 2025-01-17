import requests
import json


from defaultPixel import sendPixel

# defaults
Start = {'x': 5, 'y': 5}
xbegin = 5
xend = 180
spacing = 1

letter_bitmaps = {
    'A': [
        "001110000",
        "010001000",
        "100000100",
        "111111100",
        "100000100",
        "100000100",
        "100000100",
        "000000000",
        "000000000"
    ],
    'B': [
        "011110000",
        "010001000",
        "010001000",
        "011110000",
        "010001000",
        "010001000",
        "011110000",
        "000000000",
        "000000000"
    ],
    'C': [
        "000111000",
        "001000100",
        "010000000",
        "010000000",
        "010000000",
        "001000100",
        "000111000",
        "000000000",
        "000000000"
    ],
    'D': [
        "011110000",
        "010001000",
        "010000100",
        "010000100",
        "010000100",
        "010001000",
        "011110000",
        "000000000",
        "000000000"
    ],
    'E': [
        "011111100",
        "010000000",
        "010000000",
        "011111000",
        "010000000",
        "010000000",
        "011111100",
        "000000000",
        "000000000"
    ],
    'F': [
        "011111100",
        "010000000",
        "010000000",
        "011111000",
        "010000000",
        "010000000",
        "010000000",
        "000000000",
        "000000000"
    ],
    'G': [
        "000111000",
        "001000100",
        "010000000",
        "010011100",
        "010000100",
        "001000100",
        "000111000",
        "000000000",
        "000000000"
    ],
    'H': [
        "010000100",
        "010000100",
        "010000100",
        "011111100",
        "010000100",
        "010000100",
        "010000100",
        "000000000",
        "000000000"
    ],
    'I': [
        "001111000",
        "000100000",
        "000100000",
        "000100000",
        "000100000",
        "000100000",
        "001111000",
        "000000000",
        "000000000"
    ],
    'J': [
        "000111100",
        "000001000",
        "000001000",
        "000001000",
        "000001000",
        "010001000",
        "001110000",
        "000000000",
        "000000000"
    ],
    'K': [
        "010000100",
        "010001000",
        "010010000",
        "011100000",
        "010010000",
        "010001000",
        "010000100",
        "000000000",
        "000000000"
    ],
    'L': [
        "010000000",
        "010000000",
        "010000000",
        "010000000",
        "010000000",
        "010000000",
        "011111100",
        "000000000",
        "000000000"
    ],
    'M': [
        "010000100",
        "011001100",
        "010110100",
        "010000100",
        "010000100",
        "010000100",
        "010000100",
        "000000000",
        "000000000"
    ],
    'N': [
        "010000100",
        "011000100",
        "010100100",
        "010010100",
        "010001100",
        "010000100",
        "010000100",
        "000000000",
        "000000000"
    ],
    'O': [
        "000111000",
        "001000100",
        "010000010",
        "010000010",
        "010000010",
        "001000100",
        "000111000",
        "000000000",
        "000000000"
    ],
    'P': [
        "011111000",
        "010000100",
        "010000100",
        "011111000",
        "010000000",
        "010000000",
        "010000000",
        "000000000",
        "000000000"
    ],
    'Q': [
        "000111000",
        "001000100",
        "010000010",
        "010000010",
        "010010010",
        "001000100",
        "000111010",
        "000000000",
        "000000000"
    ],
    'R': [
        "011111000",
        "010000100",
        "010000100",
        "011111000",
        "010010000",
        "010001000",
        "010000100",
        "000000000",
        "000000000"
    ],
    'S': [
        "000111100",
        "001000000",
        "001000000",
        "000111000",
        "000000100",
        "000000100",
        "011111000",
        "000000000",
        "000000000"
    ],
    'T': [
        "011111100",
        "000100000",
        "000100000",
        "000100000",
        "000100000",
        "000100000",
        "000100000",
        "000000000",
        "000000000"
    ],
    'U': [
        "010000100",
        "010000100",
        "010000100",
        "010000100",
        "010000100",
        "010000100",
        "001111000",
        "000000000",
        "000000000"
    ],
    'V': [
        "010000100",
        "010000100",
        "010000100",
        "010000100",
        "010000100",
        "001001000",
        "000110000",
        "000000000",
        "000000000"
    ],
    'W': [
        "010000100",
        "010000100",
        "010000100",
        "010000100",
        "010110100",
        "011001100",
        "010000100",
        "000000000",
        "000000000"
    ],
    'X': [
        "010000100",
        "001001000",
        "000110000",
        "000110000",
        "000110000",
        "001001000",
        "010000100",
        "000000000",
        "000000000"
    ],
    'Y': [
        "010000100",
        "001001000",
        "000110000",
        "000100000",
        "000100000",
        "000100000",
        "000100000",
        "000000000",
        "000000000"
    ],
    'Z': [
        "011111100",
        "000000100",
        "000001000",
        "000010000",
        "000100000",
        "001000000",
        "011111100",
        "000000000",
        "000000000"
    ],
    ' ': [
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000"
    ],     
}

# Function to write a string to the canvas
def write_string_to_canvas(color, string, start_x, start_y, spacing):
    x, y = start_x, start_y
    yline = y
    for char in string:
        #check for newline
        if char == '\n':
            x = xbegin
            yline += 9 + spacing  # Move to the next line
            y = yline  # Reset y to the new line start
            continue
        # Convert lowercase to uppercase
        char = char.upper()
        if char in letter_bitmaps:
            bitmap = letter_bitmaps[char]
            for row in bitmap:
                for col_index, pixel in enumerate(row):
                    if pixel == '1':
                        # Send the pixel to the server
                        sendPixel({'x': x + col_index, 'y': y, 'color': color})
                y += 1
                # Check if the Y limit is reached
                if y >= 180:  # Assuming 180 is the Y limit
                    print("Reached Y limit, stopping.")
                    return
            x += 9 + spacing
            y = yline  # Reset y to start_y after each letter
            if x + 9 > xend:  # Check if the next letter will exceed xend
                x = xbegin
                yline += 9 + spacing  # Move to the next line
                y = yline  # Reset y to the new line start
        else:
            print(f"Character '{char}' not in bitmap.")

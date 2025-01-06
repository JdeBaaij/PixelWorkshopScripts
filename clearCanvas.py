from defaultPixel import sendPixel

#default color for off-white background
color = [245, 245, 245]

def clear_canvas():
    # Loop through each x and y coordinate to fill the entire canvas
    for x in range(199, -1, -1):
        for y in range(199, -1, -1):
            # Create a pixel for each coordinate
            pixel = {'x': x, 'y': y, 'color': color}
            # Send the pixel to the server
            sendPixel(pixel)
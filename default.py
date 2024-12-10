import requests
import json

# This is the URL of the server where we send the pixels.
url = "http://localhost:5173/api/single"
headers = {'Content-Type': 'application/json'}

# This is a function.
# We will use this function to send a pixel to the canvas.
def sendPixel(pixel):
    response = requests.post(url, headers=headers, data=json.dumps({**pixel, 'key': 'julius'}))
    print(response.content)

# First, we will create a pixel.
# This is a variable that contains the following information.
#    x: the x coordinate where we want to place the pixel.
#    y: the y coordinate where we want to place the pixel.
#    color: the color the pixel should be in RGB.
pixel = {'x': 86, 'y': 25, 'color': [255, 0, 0]}

# By passing this pixel variable to the sendPixel function, it will be sent to the server.
sendPixel(pixel)
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

# defaults
url = os.getenv('DOMAIN')
headers = {'Content-Type': 'application/json'}
color = [245, 245, 245]

def sendPixel(pixel):
    response = requests.post(url, headers=headers, data=json.dumps({**pixel, 'key': os.getenv('MASTER_KEY')}))

# Loop through each x and y coordinate to fill the entire canvas
for x in range(200):
    for y in range(200):
        # Create a pixel for each coordinate
        pixel = {'x': x, 'y': y, 'color': color}
        # Send the pixel to the server
        sendPixel(pixel)
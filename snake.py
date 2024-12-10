import requests
import json
import sys
import time
import threading

# This is the URL of the server where we send the pixels.
url = "https://pixelcorp.nl/api/single"
headers = {'Content-Type': 'application/json'}

snake_colour = [0, 255, 0]
black_color = [0, 0, 0]
background_colour = [255, 255, 255]

# This is a function.
# We will use this function to send a pixel to the canvas.
def sendPixel(pixel):
    response = requests.post(url, headers=headers, data=json.dumps({**pixel, 'key': 'WHWKIKBI'}))
    print(response.content)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_position(self, x, y):
        new_node = Node(x, y)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(f"({current.x}, {current.y})")
            current = current.next
    
    def get_last_position(self):
        current = self.head
        if current is None:
            return None
        while current.next:
            current = current.next
        return current

class Snake:
    def __init__(self, x, y, initial_direction = 'd'):
        self.positions = LinkedList()
        self.positions.add_position(x, y)  # Initial position of the snake's head
        self.current_direction = initial_direction  # Default initial direction

    def move(self):
        head = self.positions.head
        if self.current_direction == 'w':  # Move up
            new_x, new_y = head.x, head.y - 1
        elif self.current_direction == 'd':  # Move right
            new_x, new_y = head.x + 1, head.y
        elif self.current_direction == 's':  # Move down
            new_x, new_y = head.x, head.y + 1
        elif self.current_direction == 'a':  # Move left
            new_x, new_y = head.x - 1, head.y
        else:
            return  # Invalid direction, do nothing

        # Add new head position
        self.positions.add_position(new_x, new_y)
        # Remove the tail (for simplicity, assuming snake length is constant)
        self.remove_tail()

    def remove_tail(self):
        current = self.positions.head
        if current is None or current.next is None:
            return
        while current.next.next:
            current = current.next
        current.next = None
    
    def add_position(self, x, y):
        self.positions.add_position(x, y)

    def print_snake(self):
        self.positions.print_list()

def read_input(snake):
    for direction in sys.stdin:
        direction = direction.strip()
        if direction in ['w', 'a', 's', 'd']:
            snake.current_direction = direction

#snake starting positions
snake = Snake(1, 196, 'd')
snake.add_position(0, 196)


# Start a thread to read input
input_thread = threading.Thread(target=read_input, args=(snake,))
input_thread.daemon = True
input_thread.start()

# Game loop
while True:
    snake.move()
    snake.print_snake()
    # Optionally, send the new head position to the server
    head = snake.positions.head
    sendPixel({'x': head.x, 'y': head.y, 'color': snake_colour})
    # remove tail by placing background_colour at position of tail
    tail = snake.positions.get_last_position()
    sendPixel({'x': tail.x, 'y': tail.y, 'color': background_colour})
    
    time.sleep(0.2)  # Delay of 0.2 seconds
import requests
import json
import sys
import time
import threading
from defaultPixel import sendPixel

snake_colour = [0, 255, 0]
black_color = [0, 0, 0]
background_colour = [245, 245, 245]

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
    def __init__(self, x, y, initial_direction='d'):
        self.positions = LinkedList()
        self.positions.add_position(x, y)  # Initial position of the snake's head
        self.current_direction = initial_direction  # Default initial direction
        self.length = 1  # Initial length of the snake

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

        # Check for self-intersection
        if self.check_self_intersection(new_x, new_y):
            print("Game Over: Snake intersected with itself.")
            sys.exit()

        # Add new head position
        self.positions.add_position(new_x, new_y)
        # Remove the tail only if the snake's length is exceeded
        if self.length < self.get_length():
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
    
    def check_self_intersection(self, x, y):
        current = self.positions.head.next  # Start checking from the second node
        while current:
            if current.x == x and current.y == y:
                return True
            current = current.next
        return False

    def get_length(self):
        current = self.positions.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

def read_input(snake):
    while True:
        direction = sys.stdin.read(1).strip()
        if direction in ['w', 'a', 's', 'd']:
            snake.current_direction = direction

# Initialize the snake with a single position
snake = Snake(1, 196, 'd')

# Function to increase snake length every second
def increase_length(snake):
    while True:
        time.sleep(1)
        snake.length += 1

# Start a thread to increase snake length
length_thread = threading.Thread(target=increase_length, args=(snake,))
length_thread.daemon = True
length_thread.start()

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
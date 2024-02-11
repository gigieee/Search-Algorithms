import pyglet
import random

# Create a window
window = pyglet.window.Window(width=800, height=200, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a sorted list with random numbers ensuring 42 is included
numbers = sorted(random.sample(range(1, 80), 20) + [26])

# Variables to control the animation and search
left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False

def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == 26:
            found = True
        elif numbers[mid] < 26:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True

# Schedule the binary search to run every 0.5 seconds
pyglet.clock.schedule_interval(lambda dt: binary_search(), 0.5)

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # Define the position and size of each 'box'
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        # Draw the box
        if left <= i <= right and not search_complete:
            color = (255, 182, 193)
        elif i == mid and not search_complete:
            color = (255, 0, 0)
        elif found and i == mid:
            color = (0, 255, 0)
        else:
            color = (200, 200, 200)
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        # Draw the number inside the box
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.app.run()
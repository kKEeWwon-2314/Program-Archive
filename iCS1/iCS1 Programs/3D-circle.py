"""
A circle-drawing program that creates a 3D feel
"""

import stddraw

radius = 0.5
continue_drawing = True

# our main animation loop
while continue_drawing:
    stddraw.circle(0.5, 0.5, radius)
    # make the circle a little smaller
    radius = radius * 0.9

    # show the circles and pause for 500 milliseconds
    stddraw.show(500)

    # ask the user if they want to keep going
    response = input('Keep drawing circles? ')
    if response == 'n':
        continue_drawing = False
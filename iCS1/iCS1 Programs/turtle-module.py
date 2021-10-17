"""
A weird copyright from the LOGO turtle module.
"""

import stddraw
import math

class Turtle:
    """
    Basic LOGO turtle
    """
    def __init__(self, x, y):
        # stores xy coordinates
        self._x = x
        self._y = y
        self._ta = 90.0 #north

    def turn_left(self, angle):
        """
        Tell it to turn
        """
        self._ta += angle

    def move_foward(self, distance):
        """
        Move foward by distance
        """
        # calculate position
        radians = math.radians(self._ta)
        x1 = self._x + distance * math.cos(radians)
        y1 = self._y + distance * math.sin(radians)
        # draw line
        stddraw.line(self._x, self._y, x1, y1)

        self._x = x1
        self._y = y1

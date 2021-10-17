"""
This program is so that Karel could read the daily newspaper in bed.

    Author: Kevin
    Date:   March. 29, 2020
"""

from karel import *

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

begin_karel_program()

# exiting the house to get hte paper

for i in range(3):
    move()
    move()
    turn_left()

move()
pick_beeper()
turn_around()
move()
turn_right()

# returning with the paper... don't read while you walk!

for i in range(2):
    move()
    move()
    turn_right()

move()
move()
turn_left()

end_karel_program()

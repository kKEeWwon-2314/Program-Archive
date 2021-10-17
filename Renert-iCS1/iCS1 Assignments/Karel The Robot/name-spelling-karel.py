"""
This program is so that Karel could spell my name-with beepers.

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

def create_line():
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

begin_karel_program()

#making the letter K

create_line()
turn_right()
move()
move()
put_beeper()
turn_right()
move()
turn_right()
move()
put_beeper()
turn_left()
move()
move()
put_beeper()
move()
turn_left()
move()
put_beeper()

#now making the letter L

move()
move()
turn_left()
create_line()
turn_around()
move()
move()
move()
move()
turn_left()
move()
put_beeper()
move()
put_beeper()
move()

end_karel_program()

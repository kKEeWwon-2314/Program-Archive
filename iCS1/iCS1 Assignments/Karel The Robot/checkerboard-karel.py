"""
This is a program which teaches Karel to make a chessboard!

    Author: Kevin
    Date: April. 4, 2020
"""

from karel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def sweep_board():
    if facing_east():
        turn_left()
        if front_is_clear():
            move()
            turn_left()
    else:
        turn_right()
        if front_is_clear():
            move()
            turn_right()

def celebrate():
    # this command is sorta useless
    while beepers_in_bag():
        turn_right()
    
begin_karel_program()

while front_is_clear():
    put_beeper()
    move()
    if not front_is_clear():
        sweep_board()     
    else:
        move()
        if not front_is_clear():
            put_beeper()
            sweep_board()
            if front_is_clear():
                move()
celebrate()

end_karel_program()

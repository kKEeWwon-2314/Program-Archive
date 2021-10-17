"""
Karel's job is to cover a world of arbitrary size, with walled-off regions of any shap, with a single layer of beepers, wherever he is able to go. This problem lends itself most nicely to a recursive solution, one incarnation of which is this program.
"""
from karel import *

def turn_around():
    turn_left()
    turn_left()

def spread_carpet():
    # base case: if there's already carpet here, we don't need to do anything

    # general case: otherwise put some new carpet down and spread it to any adjacent cells
    if not beepers_present():
        # lay down new carpet here
        put_beeper()

        # repeat 4 times (once for each cardinal direction)
        for i in range(4):
            # check if the cell in front of us is accessible
            if front_is_clear():
                # move there
                move()
                # spread more carpet
                spread_carpet()
                # then come back to face the same way we started
                turn_around()
                move()
                turn_around()

            # turn to face the next cardinal direction
            turn_left()


begin_karel_program()

spread_carpet()

end_karel_program()
from karel import *

def turn_around():
    turn_left()
    turn_left()

def half_walk():
    """
    Have Karel walk forward until he hits a wall, then turn around and
    come back halfway (rounded up).
    """
    # base case: if we've hit the wall, turn around
    if not front_is_clear():
        turn_around()
    # general case:
    else:
        # take (up to) two steps foward
        move()
        if front_is_clear():
            move()
        # use this same instruction to solve the half way problem that remains in front of us recusively
        half_walk()
        # after we've come back half way from what was in front of us, take one more step to balance the steps we took
        move()

begin_karel_program()

half_walk()
put_beeper()

end_karel_program()
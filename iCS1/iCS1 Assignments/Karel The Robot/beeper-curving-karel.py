from karel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def sweep_wall():
    turn_right()
    move()
    turn_right()

begin_karel_program()

move()
move()
move()
turn_left()
for i in range(9):
    move()

turn_right()

while front_is_clear():
    move()
    put_beeper()

if not front_is_clear():
    turn_left()

while front_is_clear():
    move()
    if not right_is_clear():
        put_beeper()

if not front_is_clear():
    sweep_wall()

while front_is_clear():
    move()
    if not right_is_clear():
        put_beeper()

if not front_is_clear():
    turn_left()

while front_is_clear():
    move()
    if not right_is_clear():
        put_beeper()

if not front_is_clear():
    sweep_wall()

while front_is_clear():
    move()
    if not right_is_clear():
        put_beeper()

if not front_is_clear():
    turn_left()

while front_is_clear():
    move()
    if not right_is_clear():
        put_beeper()

if not front_is_clear():
    sweep_wall()

while front_is_clear():
    move()
    if not right_is_clear():
        put_beeper()

if not front_is_clear():
    turn_left()

while front_is_clear():
    move()
    if not right_is_clear():
        put_beeper()

if not front_is_clear():
    sweep_wall()

end_karel_program()

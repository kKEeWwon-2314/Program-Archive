"""
The controls module implements functions that mediate between input devices
attached to the computer and the progression of the game itself. It defines
a ControlState data type (just an aggregate record) that stores all the
controls associated with playing the game, which other modules can interpret.
[NOTE: Run the script whenpigsfly.py to play the game.]
    Author: iCS1
    Date:   July 6, 2020
"""
import pygame
from pygame.joystick import Joystick

# reference to a Joystick object to communicate with game pad if attached
_joystick = None


class ControlState:
    """
    The ConstrolState class holds all the commands we can give to our game,
    irrespective of the input device used to generate those commands. This
    makes it easier for our game to handle different input devices.
    """
    def __init__(self):
        self.tilt_up = False
        self.tilt_down = False
        self.pull = False
        self.fire = False
        self.quit = False


def initialize():
    # find any joysticks (game pads) attached to the host computer
    n = pygame.joystick.get_count()
    global _joystick
    if n > 0:
        _joystick = Joystick(0)
        _joystick.init()


def retrieve_input():
    # our job is to update the control state of our game based on key presses, etc.
    state = ControlState()
    state.fire = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state.quit = True
        elif event.type == pygame.KEYUP:
            # use the release of the space key to trigger pig release
            if event.key == pygame.K_SPACE:
                state.fire = True
        elif event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                state.fire = True

    # capture keys that we can press and hold
    pressed = pygame.key.get_pressed()
    state.tilt_up = pressed[pygame.K_LEFT]
    state.tilt_down = pressed[pygame.K_RIGHT]
    state.pull = pressed[pygame.K_SPACE]

    # take input from game pad if one was found
    if _joystick is not None:
        axis = _joystick.get_axis(0)
        if axis > 0.3:
            state.tilt_down = True
        elif axis < -0.3:
            state.tilt_up = True
        state.pull = state.pull or _joystick.get_button(0)

    return state

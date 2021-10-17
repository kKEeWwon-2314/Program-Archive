"""
The main script to run the game "When Pigs Fly", the product of a 90-minute
game jam to demonstrate the scaffolding of a game developed with the Pygame
libraries in Python.
    Author: iCS1 class
    Date:   July 6, 2020
"""

import pygame

import graphics
import controls
import animation
import sound
from gamelogic import Game
from scene import Scene

pygame.mixer.pre_init(frequency=44100, buffer=512)
pygame.init()

# initialize all our modules
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
graphics.initialize(SCREEN_WIDTH, SCREEN_HEIGHT)
sound.initialize()
controls.initialize()

# create the world and a game object
world = Scene(SCREEN_WIDTH, SCREEN_HEIGHT)
world.create_sling()
world.create_birds()

game_state = Game(world)
game_clock = pygame.time.Clock()

# run game loop
quit_game = False
while not quit_game:
    # tick the game clock
    delta_t = 0.001 * game_clock.tick(60)   # convert to seconds

    # get input
    control_state = controls.retrieve_input()
    if control_state.quit:
        quit_game = True

    # run animation and physics
    animation.move_objects(world, delta_t)
    collisions = animation.detect_collisions(world)

    # run game logic
    game_state.process_input(control_state, delta_t)
    game_state.process_collisions(collisions)
    game_state.update()

    # run cleanup on dead objects
    world.destroy_dead_entities()

    # draw graphics
    graphics.draw_scene(world)
    graphics.draw_text(game_state.current_score())
    pygame.display.flip()


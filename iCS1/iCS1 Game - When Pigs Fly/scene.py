"""
The scene module exists to keep track of all the objects ("entities") that
exist at any given time during the game. It defines an Entity data type that
stores common properties of our game objects, and a Scene data type that
encapsulates a master list of entities with the methods needed to create
and destroy them.
[NOTE: Run the script whenpigsfly.py to play the game.]
    Author: iCS1 class
    Date:   July 6, 2020
"""

import random
import math


class Entity:
    """
    The Entity class stores common properties for our game objects, including
    position, velocity, size, and other indicators on how it should be managed.
    """
    def __init__(self, kind, x, y, r=0):
        self.kind = kind
        self.frame = 0.0     # stores which frame of the animation we're on

        self.pos_x = x
        self.pos_y = y
        self.vel_x = 0
        self.vel_y = 0
        self.angle = 0
        self.radius = r

        self.scale = False
        self.kill = False
        # if we specified a radius for this object, set the scale flag so that
        # our graphics module will resize the image to the right size
        if r > 0:
            self.scale = True


class Scene:
    """
    The Scene class stores the state and some properties of our game world.
    It holds a master list of all entities that exist in the game, and provides
    operations to create, access, and destroy entities as needed.
    """
    def __init__(self, world_width, world_height):
        self._entities = []
        self._world_width = world_width
        self._world_height = world_height
        self._sling = None
        self._loaded_pig = None

    def create_sling(self):
        x = 150
        y = self._world_height - 200
        sling = Entity('sling', x, y)
        self._entities.append(sling)
        self._sling = sling

    def create_birds(self):
        # creates three bird targets for us to shoot
        w = self._world_width
        h = self._world_height
        for i in range(3):
            # generate coordinates for target
            x = random.randrange(w//2, w - 50)
            y = random.randrange(100, h - 50)
            bird = Entity('bird', x, y, 50)
            self._entities.append(bird)

    def create_explosion(self, x, y):
        explosion = Entity('explosion', x, y, 50)
        self._entities.append(explosion)

    def load_pig(self):
        # load a new pig into the sling, readying it to be fired
        if self._loaded_pig is None:
            x = self._sling.pos_x
            y = self._sling.pos_y
            self._loaded_pig = Entity('pig', x, y, 25)
            self._entities.append(self._loaded_pig)
        return self._loaded_pig

    def shoot_pig(self, speed):
        if self._loaded_pig is not None:
            pig = self._loaded_pig
            theta = math.radians(self._sling.angle)
            pig.vel_x = speed * math.cos(theta)
            pig.vel_y = -speed * math.sin(theta)
            self._loaded_pig = None

    def entities(self):
        return self._entities

    def sling(self):
        return self._sling

    def loaded_pig(self):
        return self._loaded_pig

    def size(self):
        return self._world_width, self._world_height

    def destroy_dead_entities(self):
        alive = []
        for e in self._entities:
            if not e.kill:
                alive.append(e)
        self._entities = alive
    
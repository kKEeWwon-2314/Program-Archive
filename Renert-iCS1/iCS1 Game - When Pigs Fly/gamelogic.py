"""
The gamelogic module implements much of the rules and logic that defines
what it means to play When Pigs Fly. Data values the represent the state
of the game are encapsulated with the methods that operate on them in the
Game data type defined in this module.
[NOTE: Run the script whenpigsfly.py to play the game.]
    Author: iCS1 class
    Date:   July 6, 2020
"""
import math
import sound


class Game:
    def __init__(self, world):
        self._world = world
        self._score = 0
        self._sling_stretch = 0.0

    def update(self):
        """
        This general update method is meant to be called once every game loop
        to perform general maintenance on the game logic and game state.
        """
        # our main task here is to check if there are any enemies left, and
        # if not, spawn new ones
        enemies_remaining = 0
        for e in self._world.entities():
            if e.kind == 'bird':
                enemies_remaining += 1
        if enemies_remaining == 0:
            self._world.create_birds()

    def process_input(self, control_state, delta_t):
        sling = self._world.sling()
        if control_state.tilt_up:
            sling.angle = min(sling.angle + 1, 60)
        if control_state.tilt_down:
            sling.angle = max(sling.angle - 1, 0)

        if control_state.pull:
            pig = self._world.load_pig()
            stretch = min(self._sling_stretch + delta_t, 1.0)
            displacement = stretch * 100 - 50
            theta = math.radians(sling.angle)
            pig.pos_x = sling.pos_x - displacement * math.cos(theta) - 80 * math.sin(theta)
            pig.pos_y = sling.pos_y + displacement * math.sin(theta) - 80 * math.cos(theta)
            self._sling_stretch = stretch

        if control_state.fire:
            # shoot a pig
            speed = self._sling_stretch * 400 + 20
            self._world.shoot_pig(speed)
            self._sling_stretch = 0.0
            sound.play_sound('pig')

            # cost of shooting a pig is 10 points
            if self._score > 0:
                self._score -= 10

    def process_collisions(self, collisions):
        for e1, e2 in collisions:
            # check if a pig hit a bird
            if (e1.kind == 'pig' and e2.kind == 'bird') or (e1.kind == 'bird' and e2.kind == 'pig'):
                e1.kill = True
                e2.kill = True

                # create an explosion animation
                x = 0.5 * (e1.pos_x + e2.pos_x)
                y = 0.5 * (e1.pos_y + e2.pos_y)
                self._world.create_explosion(x, y)

                # and play an explosion sound
                sound.play_sound('explosion')
                
                # count some score
                self._score += 100

    def current_score(self):
        return self._score
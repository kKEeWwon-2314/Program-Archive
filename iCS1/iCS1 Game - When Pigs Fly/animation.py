"""
The purpose of the animation module is to provide functions that take care
of animating the objects in the game, including motion and physics simulation.
[NOTE: Run the script whenpigsfly.py to play the game.]
    Author: iCS1
    Date:   July 6, 2020
"""

def move_objects(scene, delta_t):
    # animate or move or apply physics to objects in the scene
    gravity = 50    # pixels / s²
    for e in scene.entities():
        # apply gravity to pigs
        if e.kind == 'pig':
            e.vel_y += delta_t * gravity
            width, height = scene.size()
            # destroy the pig when it's off the screen
            if e.pos_x > width or e.pos_y > height:
                e.kill = True
        e.pos_x += delta_t * e.vel_x
        e.pos_y += delta_t * e.vel_y
        # update the animation frame for birds and explosions
        if e.kind == 'bird' or e.kind == 'explosion':
            e.frame += 12.0 * delta_t
            # kill explosions after 12 frames
            if e.kind == 'explosion' and e.frame > 12.0:
                e.kill = True


def detect_collisions(scene):
    # check collisions between pairs of objects
    collisions = []
    e = scene.entities()
    n = len(e)
    for i in range(n):
        e1 = e[i]
        r1 = e1.radius
        for j in range(i+1, n):
            e2 = e[j]
            # ignore collisions between objects of the same kind
            if e1.kind != e2.kind:
                r2 = e2.radius
                # if the Euclidean distance (squared) is less than the sum
                # of the objects' radii (squared), then objects are touching
                d2 = (e1.pos_x - e2.pos_x) ** 2 + (e1.pos_y - e2.pos_y) ** 2
                if d2 < (r1 + r2) ** 2:
                    collisions.append((e1, e2))
    return collisions
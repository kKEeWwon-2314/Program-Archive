"""
All the visual rendering is done through the graphics module. Functions in
this module with take the contents of the scene and draw them on the screen
according to each object's state.
[NOTE: Run the script whenpigsfly.py to play the game.]
    Author: iCS1
    Date:   July 6, 2020
"""
import pygame
from pygame.color import Color

# mapping of object kinds to their corresponding image files
_image_files = {
    'background': 'assets/background.png',
    'sling': 'assets/Slingshot.png',
#    'bird': 'assets/enemybird1.png',
    'pig': 'assets/pig_96x104.png'
}

# mapping of object kinds to frames of an animation
_animation_files = {
    'bird': 'assets/enemybird/frame-X.png',
    'explosion': 'assets/Explosion.png'
}

# maps names (e.g. entity kinds) to pygame surfaces for drawing
_images = {}

# maps entity kind to a list of pygame surfaces representing an animation
_animations = {}

# a reference to the Pygame Surface object that is our screen (game window)
_screen = None

# a font to draw text with
_font = None


def initialize(width, height):
    # create game window
    global _screen
    _screen = pygame.display.set_mode((width, height))

    # load game font
    global _font
    _font = pygame.font.Font('assets/Pacifico.ttf', 32)

    # load images
    for name, file in _image_files.items():
        _images[name] = pygame.image.load(file)

    # load enemy bird animation frames (8 total)
    bird_file = _animation_files['bird']
    bird_frames = []
    for i in range(1, 9):
        file = bird_file.replace('X', str(i))
        surface = pygame.image.load(file)
        # images are backward, so we'll flip them
        surface = pygame.transform.flip(surface, True, False)
        bird_frames.append(surface)
    _animations['bird'] = bird_frames

    # load explosion animation from file
    explosion_file = _animation_files['explosion']
    explosion_surface = pygame.image.load(explosion_file)
    explosion_frames = []
    # the explosion animation comes as 12 pictures within the same image file,
    # so we'll use pygame's Surface.subsurface to slice it up
    width, height = explosion_surface.get_size()
    width //= 12
    for i in range(12):
        region = pygame.Rect(i*width, 0, width, height)
        surface = explosion_surface.subsurface(region)
        explosion_frames.append(surface)
    _animations['explosion'] = explosion_frames


def draw_scene(scene):
    """
    Draw visuals corresponding to everything contained in the Scene object
    to the screen (game window).
    """
    # draw the background
    background = _images['background']
    _screen.blit(background, (0, -48))

    # draw all entities in our scene
    for e in scene.entities():
        surface = None

        # locate the image that matches our entity
        if e.kind in _images:
            surface = _images[e.kind]
        # or the specific frame of the animation if it's animated
        elif e.kind in _animations:
            frames = _animations[e.kind]
            surface = frames[int(e.frame) % len(frames)]
        
        # if this entity has a visual, draw it
        if surface is not None:
            # if the entity is marked to be scaled to its radius size
            if e.scale:
                w, h = surface.get_size()
                scale = 2.0 * min(e.radius / w, e.radius / h)
                surface = pygame.transform.scale(surface, (int(scale * w), int(scale * h)))
            # if the entity requires rotation
            if e.angle != 0:
                surface = pygame.transform.rotate(surface, e.angle)
            w, h = surface.get_size()
            _screen.blit(surface, (e.pos_x - w//2, e.pos_y - h//2))
    

def draw_text(score):
    """
    Uses the game font to write text messages to the screen.
    """

    # write welcome message and instructions to the top-left corner
    text = 'Welcome to When Pigs Fly by iCS1!'
    surface = _font.render(text, True, Color('navy'))
    height = surface.get_height()
    _screen.blit(surface, (10, 0))
    text = 'Press arrows to rotate and hold space to fire!'
    surface = _font.render(text, True, Color('darkred'))
    _screen.blit(surface, (10, height))

    # draw the current game score to the upper-right corner
    text = 'Score: ' + str(score)
    surface = _font.render(text, True, Color('white'))
    width = surface.get_width()
    _screen.blit(surface, (_screen.get_width() - width - 20, 0))
"""
The sound module implements functions to load and play sounds and music in
the game when desired.
[NOTE: Run the script whenpigsfly.py to play the game.]
    Author: iCS1 class
    Date:   July 6, 2020
"""
import pygame
from pygame.mixer import Sound

# mapping from sound names to their corresponding sound files
_sound_files = {
    'pig': 'assets/Mudchute_pig_1.wav',
    'explosion': 'assets/explosion.wav'
}

# mapping from sound names to pygame Sound() objects
_sounds = {}

def initialize():
    # load each sound file in the master list and create playable Sound objects
    for name, file in _sound_files.items():
        _sounds[name] = Sound(file)
        _sounds[name].set_volume(0.4)

    # load and play the music file in a loop
    pygame.mixer.music.load('assets/Intro Theme.wav')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)


def play_sound(name):
    """
    Play the sound requested by the given name.
    """
    if name in _sounds:
        _sounds[name].play()

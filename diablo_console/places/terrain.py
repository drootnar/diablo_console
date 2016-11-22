from ..const import *

__all__ = ['Lake', 'Ocean', 'Dirt', 'Forest', 'Mountain', 'MountainPeak', 'Grass']


class Place:
    pass


class Terrain(Place):
    type = 'terrain'


class Lake(Terrain):
    name = 'lake'
    input_key = 'w'
    output_key = '.'
    description = 'There is a lake over there'
    efect = C_FILL_CYAN
    enterable = False


class Ocean(Terrain):
    name = 'ocean'
    input_key = 'W'
    output_key = '.'
    description = 'Swim swim swim. Cannot...'
    efect = C_FILL_BLUE
    enterable = False


class Dirt(Terrain):
    name = 'dirt'
    input_key = '.'
    output_key = ' '
    description = 'Just dirt'
    efect = C_WHITE
    enterable = True


class Forest(Terrain):
    name = 'forest'
    input_key = 'f'
    output_key = 'f'
    description = 'You see small forest'
    efect = C_FILL_GREEN
    enterable = True


class Mountain(Terrain):
    name = 'mountain'
    input_key = '^'
    output_key = '^'
    description = 'Mountains begin'
    efect = C_WHITE
    enterable = False


class MountainPeak(Terrain):
    name = 'mountain peak'
    input_key = '!'
    output_key = '!'
    description = 'Here is a mountain peak'
    efect = C_FILL_WHITE
    enterable = False


class Grass(Terrain):
    name = 'grass'
    input_key = 'g'
    output_key = '.'
    description = 'You are walking through the grass carpet.'
    efect = C_GREEN
    enterable = True

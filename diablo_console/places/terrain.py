from ..const import *

__all__ = ['Lake', 'Ocean', 'Dirt', 'Forest', 'Mountain', 'MountainPeak', 'Grass']

class Terrain:
    type = 'terrain'


class Lake(Terrain):
    name = 'lake'
    key = 'w'
    description = 'There is a lake over there'
    efect = C_FILL_CYAN
    enterable = False


class Ocean(Terrain):
    name = 'ocean'
    key = 'W'
    description = 'Swim swim swim. Cannot...'
    efect = C_FILL_BLUE
    enterable = False


class Dirt(Terrain):
    name = 'dirt'
    key = ' '
    description = 'Just dirt'
    efect = C_WHITE
    enterable = True


class Forest(Terrain):
    name = 'forest'
    key = 'f'
    description = 'You see small forest'
    efect = C_FILL_GREEN
    enterable = True


class Mountain(Terrain):
    name = 'mountain'
    key = '^'
    description = 'Mountains begin'
    efect = C_WHITE
    enterable = False


class MountainPeak(Terrain):
    name = 'mountain peak'
    key = '!'
    description = 'Here is a mountain peak'
    efect = C_FILL_WHITE
    enterable = False


class Grass(Terrain):
    name = 'grass'
    key = '.'
    description = 'You are walking through the grass carpet.'
    efect = C_GREEN
    enterable = True
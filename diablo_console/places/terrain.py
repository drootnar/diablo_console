from ..const import *

__all__ = ['Place', 'Lake', 'Ocean', 'Dirt']

class Place:
    pass


class Lake(Place):
    name = 'lake'
    key = 'w'
    description = 'There is a lake over there'
    efect = C_FILL_CYAN
    enterable = False


class Ocean(Place):
    name = 'ocean'
    key = 'W'
    description = 'Swim swim swim. Cannot...'
    efect = C_FILL_BLUE
    enterable = False


class Dirt(Place):
    name = 'dirt'
    key = ' '
    description = 'Just dirt'
    efect = C_WHITE
    enterable = True
from ..const import *
from .terrain import Place

__all__ = [
    'RoofLeft', 'RoofRight', 'HouseVert', 'HouseHor', 'HouseBottomMiddle', 'HouseUpMiddle',
    'HouseLeftUp', 'HouseLeftBottom', 'HouseLeftMiddle', 'HouseRightUp', 'HouseRightBottom',
    'HouseRightMiddle', 'HouseIntersection', 'HouseWall1', 'HouseWall2', 'HouseWall3']

class Building(Place):
    type = 'building'


class RoofLeft(Building):
    name = 'roof'
    key = '/'
    description = 'That is a roof'
    efect = C_MAGENTA
    enterable = False


class RoofRight(Building):
    name = 'roof'
    key = '\\'
    description = 'That is a roof'
    efect = C_MAGENTA
    enterable = False


class House(Building):
    name = 'house'
    description = 'That is a house'
    efect = C_MAGENTA
    enterable = False


class HouseVert(House):
    key = '┃'
    

class HouseHor(House):
    key = '━'


class HouseBottomMiddle(House):
    key = '┻'


class HouseUpMiddle(House):
    key = '┳'


class HouseLeftUp(House):
    key = '┏'


class HouseLeftBottom(House):
    key = '┗'


class HouseLeftMiddle(House):
    key = '┣'


class HouseRightUp(House):
    key = '┓'


class HouseRightBottom(House):
    key = '┛'


class HouseRightMiddle(House):
    key = '┫'


class HouseIntersection(House):
    key = '╋'


class HouseWall1(House):
    key = '░'


class HouseWall2(House):
    key = '▒'


class HouseWall3(House):
    key = '▓'
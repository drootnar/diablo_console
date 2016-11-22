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
    input_key = '/'
    output_key = '/'
    description = 'That is a roof'
    efect = C_MAGENTA
    enterable = False


class RoofRight(Building):
    name = 'roof'
    input_key = '\\'
    output_key = '\\'
    description = 'That is a roof'
    efect = C_MAGENTA
    enterable = False


class House(Building):
    name = 'house'
    description = 'That is a house'
    efect = C_MAGENTA
    enterable = False


class HouseVert(House):
    input_key = '┃'
    output_key = '┃'
    

class HouseHor(House):
    input_key = '━'
    output_key = '━'


class HouseBottomMiddle(House):
    input_key = '━'
    output_key = '━'


class HouseUpMiddle(House):
    input_key = '┳'
    output_key = '┳'

class HouseLeftUp(House):
    input_key = '┏'
    output_key = '┏'


class HouseLeftBottom(House):
    input_key = '┗'
    output_key = '┗'


class HouseLeftMiddle(House):
    input_key = '┣'
    output_key = '┣'


class HouseRightUp(House):
    input_key = '┓'
    output_key = '┓'


class HouseRightBottom(House):
    input_key = '┛'
    output_key = '┛'


class HouseRightMiddle(House):
    input_key = '┫'
    output_key = '┫'


class HouseIntersection(House):
    input_key = '╋'
    output_key = '╋'


class HouseWall1(House):
    input_key = '░'
    output_key = '░'


class HouseWall2(House):
    input_key = '▒'
    output_key = '▒'


class HouseWall3(House):
    input_key = '▓'
    output_key = '▓'
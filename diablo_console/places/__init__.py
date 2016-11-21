from .terrain import *
from .building import *

places = {
    'w': Lake,
    'W': Ocean,
    '.': Dirt,
    'f': Forest,
    '^': Mountain,
    '!': MountainPeak,
    'g': Grass,
    '/': RoofLeft,
    '\\': RoofRight,
    '┃': HouseVert,
    '━': HouseHor,
    '┻': HouseBottomMiddle,
    '┳': HouseUpMiddle,
    '┏': HouseLeftUp,
    '┗': HouseLeftBottom,
    '┣': HouseLeftMiddle,
    '┓': HouseRightUp,
    '┛': HouseRightBottom,
    '┫': HouseRightMiddle,
    '╋': HouseIntersection,
    '░': HouseWall1,
    '▒': HouseWall2,
    '▓': HouseWall3
}
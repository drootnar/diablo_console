import random

from .utils import load_level

__all__ = ['GameState']


class GameState:
    '''
    Simple GameState object
    '''
    def __init__(self, canvas):
        self.x = 0
        self.y = 0
        self.screen_x = 0
        self.screen_y = 0
        self.screen_width = canvas.board.width - 2
        self.screen_height = canvas.board.height - 2
        (self.points, self.level_x, self.level_y) = load_level('level3')
import random

from .utils import load_level

__all__ = ['GameState']


class GameState:
    '''
    Simple GameState object
    '''
    def __init__(self):
        self.x = 0
        self.y = 0
        self.points = load_level('level1')
import random

__all__ = ['GameState']


class GameState:
    '''
    Simple GameState object
    '''
    def __init__(self):
        self.x = 0
        self.y = 0
        self.points = [[random.choice(' . *') for i in range(1, 201)] for x in range(1, 101)]
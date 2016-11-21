import curses

from .windows import Window
from ..errors import ViewError

__all__ = ['Canvas']


class Canvas:
    def __init__(self):
        # SIDE_PANEL_WIDTH = 30
        # LOGGER_HEIGHT = 3
        self.stack = []
        self.obj = curses.initscr()
        self.obj.keypad(True)
        self.obj.immedok(True)
        (self.max_y, self.max_x) = self.obj.getmaxyx()
        # if self.max_y < 10 or self.max_x < 40:
        #     raise ViewError('Terminal size too small')
        # self.board = Window(self, x=0, y=0, width=self.max_x-SIDE_PANEL_WIDTH, height=self.max_y-LOGGER_HEIGHT, title='map')
        # self.side = Window(self, x=self.max_x-SIDE_PANEL_WIDTH, y=0, width=SIDE_PANEL_WIDTH, height=self.max_y-LOGGER_HEIGHT, title='menu')
        # self.logger = Window(self, x=0, y=self.max_y-LOGGER_HEIGHT, width=self.max_x, height=LOGGER_HEIGHT, title='logger')
        self.focus = None

    def set_focus(self, window):
        self.focus = window

    def get_focus(self):
        return self.focus

    def input(self):
        return self.obj.getch()

    def refresh(self):
        self.obj.refresh()

    def move(self, y, x):
        self.obj.move(y, x)

    def close(self):
        curses.endwin()

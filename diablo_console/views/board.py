import curses

from .windows import Window
from ..errors import ViewError
from ..const import *

__all__ = ['Canvas', 'CanvasWindow', 'LoggerWindow']


class Canvas:
    '''
    Basic class determining console screen.
    Store max_x, max_y of the screen and focused (active) window.
    '''
    def __init__(self):
        self.stack = []
        self.obj = curses.initscr()
        self.obj.keypad(True)
        self.obj.immedok(True)
        (self.max_y, self.max_x) = self.obj.getmaxyx()
        if self.max_y < 10 or self.max_x < 40:
            raise ViewError('Terminal size too small')
        self.board = CanvasWindow(self, x=0, y=0, width=self.max_x-SIDE_PANEL_WIDTH, height=self.max_y-LOGGER_HEIGHT, title='map')
        self.side = CanvasWindow(self, x=self.max_x-SIDE_PANEL_WIDTH, y=0, width=SIDE_PANEL_WIDTH, height=self.max_y-LOGGER_HEIGHT, title='menu')
        self.logger = LoggerWindow(self, x=0, y=self.max_y-LOGGER_HEIGHT, width=self.max_x, height=LOGGER_HEIGHT, title='logger')
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

    def render(self, state):
        for y, line in enumerate(state.points):
            if y > self.board.height -3:
                break
            for x, char in enumerate(line):
                if x > self.board.width -3:
                    break
                self.board.obj.addnstr(y+1, x+1, char, 1)
        self.board.obj.refresh()


class CanvasWindow(Window):
    '''
    Board (constant) windows placed on canvas.
    '''
    def __init__(self, *args, **kwargs):
        super(CanvasWindow, self).__init__(*args, **kwargs)

    def create(self):
        self.obj = self.canvas.obj.derwin(self.height, self.width, self.y, self.x)
        self.obj.border(0)
        if self.title:
            self.obj.addstr(0, 1, '[{}]'.format(self.title[:self.width-4]), C_BOLD | C_UNDERLINE)
        self.obj.refresh()


class LoggerWindow(CanvasWindow):
    '''
    Logger Window
    '''
    def __init__(self, *args, **kwargs):
        super(LoggerWindow, self).__init__(*args, **kwargs)

    def display(self, text):
        self.obj.addnstr(1, 1, text, self.width-2)
        self.obj.refresh()

import curses
import math

from .windows import Window, Area, Separator
from ..errors import ViewError
from ..const import *

__all__ = ['Canvas', 'BoardWindow', 'SidePanelWindow', 'LoggerWindow']


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
        if self.max_y < TERMINAL_MIN_Y or self.max_x < TERMINAL_MIN_X:
            raise ViewError('Terminal size too small')
        self.board = BoardWindow(
            self, x=0, y=0,
            width=self.max_x-SIDE_PANEL_WIDTH, height=self.max_y-LOGGER_HEIGHT, title='map')
        self.side = SidePanelWindow(
            self, x=self.max_x-SIDE_PANEL_WIDTH, y=0, width=SIDE_PANEL_WIDTH,
            height=self.max_y-LOGGER_HEIGHT, title='inventory')
        self.logger = LoggerWindow(
            self, x=0, y=self.max_y-LOGGER_HEIGHT,
            width=self.max_x, height=LOGGER_HEIGHT, title='logger')
        self.focus = None

    def set_focus(self, window):
        self.focus = window

    def get_focus(self):
        return self.focus

    def input(self):
        return self.obj.getch()

    def refresh(self):
        self.obj.refresh()

    def close(self):
        curses.endwin()

    def render(self, state):
        self.side.render(state)
        self.board.render(state)


class BoardWindow(Window):
    '''
    Board (constant) window placed on canvas.
    '''
    def __init__(self, *args, **kwargs):
        super(BoardWindow, self).__init__(*args, **kwargs)
        self.max_x = self.width-3
        self.max_y = self.height-3

    def create(self):
        self.obj = self.canvas.obj.derwin(self.height, self.width, self.y, self.x)
        self.obj.border(0)
        if self.title:
            self.obj.addstr(0, 1, '[{}]'.format(self.title[:self.width-4]), C_BOLD | C_UNDERLINE)
        self.obj.refresh()

    def render(self, state):
        screen_x = max(0, state.x - math.floor(0.5 * state.screen_width))
        if screen_x + state.screen_width >= state.level_x:
            screen_x = state.level_x - state.screen_width
        screen_y = max(0, state.y - math.floor(0.5 * state.screen_height))
        if screen_y + state.screen_height >= state.level_y:
            screen_y = state.level_y - state.screen_height
        # self.canvas.logger.display('{} {} {} {}'.format(screen_x, screen_y, screen_x+state.screen_width, screen_y+state.screen_height))
        for y, line in enumerate(state.points[screen_y:screen_y+state.screen_height]):
            for x, char in enumerate(line[screen_x:screen_x+state.screen_width]):
                self.obj.addnstr(y+1, x+1, char, 1)
        self.obj.move(state.y+1-screen_y, state.x+1-screen_x)
        self.canvas.logger.coordinate(state.x, state.y)
        self.obj.refresh()


class SidePanelWindow(Window):
    '''
    SidePanel windows placed on canvas.
    '''
    def __init__(self, *args, **kwargs):
        super(SidePanelWindow, self).__init__(*args, **kwargs)
        self.max_x = self.width-3
        self.max_y = self.height-3
        self.title = Area(self, align='up', size=5)
        self.title.display_from_file('title', efect=C_RED | C_BOLD)
        Separator(self, align='up')
        self.stats = Area(self, align='up', size=4)
        self.inv = Area(self, align='up', size=4)
        self.options = Area(self, align='bottom', size=4)
        self.options.display_lines([
            '                            ',
            'C - character    J - journal', 
            'I - inventory       M - menu',
            '                            '], 
            C_WHITE | C_REVERSE)

    def create(self):
        self.obj = self.canvas.obj.derwin(self.height, self.width, self.y, self.x)
        self.obj.border(0)
        if self.title:
            self.obj.addstr(0, 1, '[{}]'.format(self.title[:self.width-4]), C_BOLD | C_UNDERLINE)
        self.obj.refresh()

    def render(self, state):
        self.stats.display_table(
            [
                {'left': 'stregnth', 'right': 50},
                {'left': 'mana', 'right': 100},
                {'left': 'vitality', 'right': 80}
            ],
            efect=(C_WHITE, C_RED | C_BOLD), offset=15)
        self.inv.display_lines(['1', '2', '3', '4'])


class LoggerWindow(BoardWindow):
    '''
    Logger Window
    '''
    def __init__(self, *args, **kwargs):
        super(LoggerWindow, self).__init__(*args, **kwargs)

    def coordinate(self, x, y):
        self.obj.addstr(1, 1, " "*10)
        self.obj.addnstr(1, 1, '({},{})'.format(x, y), 10)
        self.obj.refresh()

    def display(self, text):
        self.obj.addstr(1, 11, " "*(self.width-12))
        self.obj.addnstr(1, 11, text, self.width-12)
        self.obj.refresh()

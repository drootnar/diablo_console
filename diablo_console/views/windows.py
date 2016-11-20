import operator
import curses

from ..const import *

__all__ = ['Window', 'Area', 'Separator', 'ButtonWindow']


class Window:
    ''' Basic window class
    Free space is without border
    '''
    def __init__(self, canvas, *args, **kwargs):
        self.canvas = canvas
        canvas.stack.append(self)
        self.width = kwargs.get('width', 10)
        self.height = kwargs.get('height', 10)
        self.x = kwargs.get('x', self._center_x())
        self.y = kwargs.get('y', self._center_y())
        self.free_space = {'min_x': 1, 'min_y': 1, 'max_x': self.width-2, 'max_y': self.height-2}
        self.title = kwargs.get('title')
        self.create()

    def _center_x(self):
        (parent_y, parent_x) = self.canvas.max_y, self.canvas.max_x
        return int((parent_x / 2) - (self.width / 2))

    def _center_y(self):
        (parent_y, parent_x) = self.canvas.max_y, self.canvas.max_x
        return int((parent_y / 2) - (self.height / 2))

    def create(self):
        self.obj = curses.newwin(self.height, self.width, self.y, self.x)
        self.obj.border(0)
        if self.title:
            self.obj.addstr(0, 1, '[{}]'.format(self.title[:self.width-4]), C_CYAN)
        self.obj.refresh()

    def destroy(self):
        self.obj.erase()
        self.canvas.refresh()

    def fill(self):
        for y in range(self.free_space['min_y'], self.free_space['max_y'] + 1):
            self.obj.addstr(y, self.free_space['min_x'], ' '*(self.free_space['max_x'] - self.free_space['min_x'] + 1), C_FILL_MAGENTA)
        self.obj.refresh()

    def change_free_space(self, action='inc', **kwargs):
        actions ={
            'inc': operator.add,
            'dec': operator.sub
        }
        if 'min_x' in kwargs:
            self.free_space['min_x'] = actions[action](self.free_space['min_x'], kwargs['min_x'])
        if 'min_y' in kwargs:
            self.free_space['min_y'] = actions[action](self.free_space['min_y'], kwargs['min_y'])
        if 'max_x' in kwargs:
            self.free_space['max_x'] = actions[action](self.free_space['max_x'], kwargs['max_x'])
        if 'max_y' in kwargs:
            self.free_space['max_y'] = actions[action](self.free_space['max_y'], kwargs['max_y'])


class ButtonWindow(Window):
    def __init__(self, *args, **kwargs):
        super(ButtonWindow, self).__init__(*args, **kwargs)
        self.buttons = Area(window=self, align='bottom', size=1)
        separator = Separator(self, align='botttom')

class Area:
    def __init__(self, window, align, size):
        self.window = window
        if align == 'up':
            self.x = window.free_space['min_x']
            self.y = window.free_space['min_y']
            self.height = size
            self.width = window.free_space['max_x']
            window.change_free_space(action='inc', min_y=size)
        elif align == 'left':
            self.x = window.free_space['min_x']
            self.y = window.free_space['min_y']
            self.height = window.free_space['max_y']
            self.width = size
            window.change_free_space(action='inc', min_x=size)
        elif align == 'right':
            self.x = window.free_space['max_x'] - size
            self.y = window.free_space['min_y']
            self.height = window.free_space['max_y']
            self.width = size
            window.change_free_space(action='dec', max_x=size)
        else:
            self.x = window.free_space['min_x']
            self.y = window.free_space['max_y'] - size
            self.height = size
            self.width = window.free_space['max_x']
            window.change_free_space(action='dec', max_y=size)

        self.obj = self.window.obj.derwin(self.height, self.width, self.y, self.x)
        self.obj.refresh()

    def fill(self):
        for y in range(0, self.height-1):
            self.obj.addstr(y, 0, ' '*(self.width), C_FILL)
        self.obj.addstr(self.height-1, 0, ' '*(self.width-1), C_FILL)
        self.obj.refresh()

    def display(self, text):
        for line_no, i in enumerate(range(0, len(text), self.width)):
            if line_no + 1 > self.height + 1:
                break
            else:
                self.obj.addnstr(line_no, 0, text[i:i+self.width], self.width)
        self.obj.refresh()


class Separator:
    def __init__(self, window, align, char=None):
        if char:
            char = char
        else:
            if align == 'left' or align == 'right':
                char = curses.ACS_VLINE
            else:
                char = curses.ACS_HLINE
        self.window = window
        if align == 'up':
            window.obj.hline(
                window.free_space['min_y'], window.free_space['min_x'],
                char, window.free_space['max_x'] - window.free_space['min_x'] + 1
            )
            window.change_free_space(action='inc', min_y=1)
        elif align == 'left':
            window.obj.vline(
                window.free_space['min_y'], window.free_space['min_x'],
                char, window.free_space['max_y'] - window.free_space['min_y'] + 1
            )
            window.change_free_space(action='inc', min_x=1)
        elif align == 'right':
            window.obj.vline(
                window.free_space['min_y'], window.free_space['max_x'],
                char, window.free_space['max_y'] - window.free_space['min_y'] + 1
            )
            window.change_free_space(action='dec', max_x=1)

        else:
            window.obj.hline(
                window.free_space['max_y'], window.free_space['min_x'],
                char, window.free_space['max_x'] - window.free_space['min_x'] + 1
            )
            window.change_free_space(action='dec', max_y=1)
        self.window.obj.refresh()

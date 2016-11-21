import operator
import curses

from ..const import *

__all__ = ['Window', 'Area', 'Separator', 'ButtonWindow', 'TextWindow']


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
        self.keys = {}
        self.create()

    def _center_x(self):
        (parent_y, parent_x) = self.canvas.max_y, self.canvas.max_x
        return int((parent_x / 2) - (self.width / 2))

    def _center_y(self):
        (parent_y, parent_x) = self.canvas.max_y, self.canvas.max_x
        return int((parent_y / 2) - (self.height / 2))

    def create(self):
        self.logger = self.canvas.logger
        self.obj = curses.newwin(self.height, self.width, self.y, self.x)
        self.obj.border(0)
        if self.title:
            self.obj.addstr(0, 1, '[{}]'.format(self.title[:self.width-4]), C_BOLD | C_UNDERLINE)
        self.obj.refresh()

    def destroy(self):
        del self.obj
        self.canvas.obj.touchwin()
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
    '''
    Window with button area at the bottom.
    Expose method add_button.
    '''
    def __init__(self, *args, **kwargs):
        super(ButtonWindow, self).__init__(*args, **kwargs)
        self.button_area = Area(window=self, align='bottom', size=1)
        separator = Separator(self, align='botttom')
        self.buttons = []

    def add_button(self, button):
        y = self.height - 2
        x = 2
        self.buttons.append(button)
        self.keys[button.key] = button.action
        for button in self.buttons:
            offset = button.render(y, x)
            x += offset + 1
        self.obj.refresh()


class TextWindow(ButtonWindow):
    '''
    Window with text area and button area
    '''
    def __init__(self, *args, **kwargs):
        super(TextWindow, self).__init__(*args, **kwargs)
        self.text = Area(self, align='up', size=self.height-4)


class Area:
    '''
    Basic class to define area inside window
    '''
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
            self.obj.addstr(y, 0, ' '*(self.width), C_FILL_YELLOW)
        self.obj.addstr(self.height-1, 0, ' '*(self.width-1), C_FILL_YELLOW)
        self.obj.refresh()

    def display(self, text):
        for line_no, i in enumerate(range(0, len(text), self.width)):
            if line_no == self.height -1:
                self.obj.addnstr(line_no, 0, text[i:i+self.width], self.width-1)
                break
            else:
                self.obj.addnstr(line_no, 0, text[i:i+self.width], self.width)
        self.obj.refresh()

    def display_lines(self, text_lines=None, efect=C_WHITE):
        if text_lines:
            for line_no, line in enumerate(text_lines):
                if line_no == self.height -1:
                    self.obj.addnstr(line_no, 0, str(line), self.width-1, efect)
                    break
                else:
                    self.obj.addnstr(line_no, 0, str(line), self.width-1, efect)
        self.obj.refresh()

    def display_table(self, data, offset=None, efect=None):
        if isinstance(efect, tuple):
            left_efect = efect[0]
            right_efect = efect[1]
        elif isinstance(efect, int):
            left_efect = efect
            right_efect = efect
        else:
            left_efect = C_WHITE
            right_efect = C_WHITE

        if not offset:
            offset = max([len(row['left']) for row in data]) + 1
        for line_no, row in enumerate(data):
            if line_no == self.height -1:
                self.obj.addnstr(line_no, 0, str(row['left']), offset, left_efect)
                self.obj.addnstr(line_no, offset, str(row['right']), self.width - offset, right_efect)
                break
            else:
                self.obj.addnstr(line_no, 0, str(row['left']), offset, left_efect)
                self.obj.addnstr(line_no, offset, str(row['right']), self.width - offset, right_efect)
        self.obj.refresh()

    def display_from_file(self, file_object, efect=C_WHITE):
        with open('diablo_console/images/{}.asc'.format(file_object)) as f:
            for line_no, line in enumerate(f):
                if line_no == self.height -1:
                    self.obj.addnstr(line_no, 0, line, self.width-1, efect)
                    break
                else:
                    self.obj.addnstr(line_no, 0, line, self.width-1, efect)
        self.obj.refresh()


class Separator:
    '''
    Simple seprator object.
    '''
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

import curses

__all__ = ['Area', 'Window', 'TextWindow']

class Area:
    def __init__(self, window, y, x, width, height):
        self.window = window
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.obj = self.window.obj.derwin(self.height, self.width, self.y, self.x)
        self.obj.refresh()

    def display(self, text, y=None, x=None):
        if y and x:
            self.obj.addnstr(y, x, text, self.width)
        else:
            for line, i in enumerate(range(0, len(text), self.width-1)):
                if line + 1 > self.height:
                    break
                else:
                    self.obj.addnstr(line, 0, text[i:i+self.width-1], self.width-1)
        self.obj.refresh()

    def clear(self):
        for y in range(0, self.height-1):
            self.obj.addnstr(y, 0, " "*(self.width-1), self.width)

        self.obj.refresh()


class Window:
    ''' Basic window class'''
    def __init__(self, canvas, *args, **kwargs):
        self.canvas = canvas
        canvas.stack.append(self)
        self.width = kwargs.get('width', 10)
        self.height = kwargs.get('height', 10)
        self.x = kwargs.get('x', self._center_x())
        self.y = kwargs.get('y', self._center_y())
        self.create()

    def _center_x(self):
        (parent_y, parent_x) = self.canvas.s.getmaxyx()
        return int((parent_x / 2) - (self.width / 2))

    def _center_y(self):
        (parent_y, parent_x) = self.canvas.s.getmaxyx()
        return int((parent_y / 2) - (self.height / 2))

    def create(self):
        self.obj = curses.newwin(self.height, self.width, self.y, self.x)
        self.obj.border(0)
        self.obj.refresh()

    def destroy(self):
        self.obj.erase()
        self.canvas.refresh()

class TextWindow(Window):
    '''TextWindow with one text area covering all window'''
    def __init__(self, *args, **kwargs):
        super(TextWindow, self).__init__(*args, **kwargs)
        self.area = Area(window=self, y=1, x=1, height=self.height-1, width=self.width-1)
        if 'text' in kwargs:
            self.area.display(kwargs['text'])
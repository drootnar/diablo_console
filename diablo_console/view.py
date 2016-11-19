import curses

__all__ = ['Canvas']

class Canvas:

    MAX_Y = 30
    MAX_X = 30

    def __init__(self):
        self.s = curses.initscr()
        curses.start_color()
        self.s.keypad(True)
        self.s.immedok(True)
        self.refresh()
        self.diff_x = 1
        self.diff_y = 1
        self.stack = []

    def refresh(self):
        self.s.refresh()
        self.s.border(0)

    def render(self, state):
        self.refresh()
        for y, x_row in enumerate(state.points):
            self.s.addstr(y + self.diff_y, self.diff_x, "".join(str(point) for point in x_row))

    def set_player(self, state):
        self.paint(10,40, str(state.x))
        self.paint(15,40, str(state.y))
        self.s.move(state.y + self.diff_y, state.x + self.diff_x)

    def input(self):
        return self.s.getch()

    def paint(self, y, x, text):
        self.s.addstr(y, x, text)


    def close(self):
        curses.endwin()





import curses
from .view import Canvas
from .views.windows import Window, Separator

__all__ = ['GameLoop', 'GameState']


class GameLoop:
    def __init__(self):
        self.canvas = Canvas()
        self.state = GameState()

    def run(self):
        x = None
        while True:
            x = self.canvas.input()
            if self.state.focus == GameState.FOCUS_WINDOW:
                if x == ord('l'):
                    window = self.canvas.stack.pop()
                    window.destroy()
                    window = Window(self.canvas, width=20, height=8, title='Window')
                    Separator(window, align='left')
                    window.fill()
                    self.state.focus = GameState.FOCUS_WINDOW
                elif x == ord('r'):
                    window = self.canvas.stack.pop()
                    window.destroy()
                    window = Window(self.canvas, width=20, height=8, title='Window')
                    Separator(window, align='right')
                    window.fill()
                    self.state.focus = GameState.FOCUS_WINDOW
                elif x == ord('u'):
                    window = self.canvas.stack.pop()
                    window.destroy()
                    window = Window(self.canvas, width=20, height=8, title='Window')
                    Separator(window, align='up')
                    window.fill()
                    self.state.focus = GameState.FOCUS_WINDOW
                elif x == ord('b'):
                    window = self.canvas.stack.pop()
                    window.destroy()
                    window = Window(self.canvas, width=20, height=8, title='Window')
                    Separator(window, align='bottom')
                    window.fill()
                    self.state.focus = GameState.FOCUS_WINDOW
                elif x == ord('q'):
                    window = self.canvas.stack.pop()
                    window.destroy()
                    self.state.focus = GameState.FOCUS_MAP
            elif self.state.focus == GameState.FOCUS_MAP:
                self.canvas.render(self.state)
                if x == ord('w'):
                    self.state.y = max(self.state.y - 1, 0)
                    self.canvas.set_player(self.state)
                elif x == ord('s'):
                    self.state.y = min(self.state.y + 1, self.canvas.MAX_Y)
                    self.canvas.set_player(self.state)
                elif x == ord('a'):
                    self.state.x = max(self.state.x - 1, 0)
                    self.canvas.set_player(self.state)
                elif x == ord('d'):
                    self.state.x = min(self.state.x + 1, self.canvas.MAX_X)
                    self.canvas.set_player(self.state)
                elif x == ord('1'):
                    window = Window(self.canvas, width=20, height=8, title='Window')
                    window.fill()
                    self.state.focus = GameState.FOCUS_WINDOW
                elif x == ord('2'):
                    window = Window(self.canvas, width=20, height=20, title='Window')
                    Separator(window, align='left')
                    Separator(window, align='right')
                    window.fill()
                    self.state.focus = GameState.FOCUS_WINDOW
                elif x == ord('q'):
                    window = TextWindow(self.canvas, width=20, height=3, text='Dziękuję za grę')
                    break
                else:
                    self.canvas.paint(3, 3, "Inne")
        self.canvas.close()

class GameState:

    FOCUS_MAP = 'map'
    FOCUS_WINDOW = 'window'

    def __init__(self):
        self.x = 0
        self.y = 0
        self.points = [[(x % i) for i in range(1, 11)] for x in range(1, 12)]
        self.focus = self.FOCUS_MAP
        
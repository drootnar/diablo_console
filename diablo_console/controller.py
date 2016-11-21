import curses
from .state import GameState
from .views.windows import *
from .views.board import Canvas
from .views.buttons import Button, OKButton, LoggerButton
from .const import *

__all__ = ['GameLoop', 'GameState']


class GameLoop:
    '''
    Consist of canvas object (visualization) and state object (state of the app)
    Expose method run to run gameloop, get pressed key and route to action
    '''
    def __init__(self):
        self.canvas = Canvas()
        self.state = GameState()

    def run(self):
        x = None
        self.canvas.render(self.state)
        while True:
            x = self.canvas.input()
            focused_window = self.canvas.get_focus()
            if not focused_window and x == K_ESCAPE:
                self.handle_exit()
                break
            if not focused_window:
                self.handle_main_screen(x)
            else:
                self.handle_focus_window(focused_window, x)
        self.canvas.close()

    def handle_main_screen(self, x):
        # moving player
        if x == ord('a'):
            self.state.x = max(self.state.x - 1, 0)
            self.canvas.render(self.state)
        elif x == ord('d'):
            self.state.x = min(self.state.x + 1, self.canvas.board.max_x)
            self.canvas.render(self.state)
        elif x == ord('w'):
            self.state.y = max(self.state.y - 1, 0)
            self.canvas.render(self.state)
        elif x == ord('s'):
            self.state.y = min(self.state.y + 1, self.canvas.board.max_y)
            self.canvas.render(self.state)
        # other action
        elif x == ord('c'):
            window = ButtonWindow(self.canvas, width=60, height=20, title='Your character')
            window.add_button(OKButton(window))
            self.canvas.set_focus(window)
        elif x == ord('j'):
            window = ButtonWindow(self.canvas, width=60, height=20, title='Journal')
            window.add_button(OKButton(window))
            self.canvas.set_focus(window)
        elif x == ord('i'):
            window = ButtonWindow(self.canvas, width=60, height=20, title='Inventory')
            window.add_button(OKButton(window))
            self.canvas.set_focus(window)
        elif x == ord('m'):
            window = ButtonWindow(self.canvas, width=60, height=20, title='Menu')
            window.add_button(OKButton(window))
            self.canvas.set_focus(window)
        elif x == ord('1'):
            window = Window(self.canvas, width=20, height=8, title='Window')
            Area(window, align='up', size=3)
            window.fill()
            self.canvas.set_focus(window)
        elif x == ord('2'):
            window = Window(self.canvas, width=20, height=8, title='Window')
            Area(window, align='right', size=3)
            window.fill()
            self.canvas.set_focus(window)
        elif x == ord('3'):
            window = Window(self.canvas, width=20, height=8, title='Window')
            Area(window, align='bottom', size=3)
            window.fill()
            self.canvas.set_focus(window)
        elif x == ord('4'):
            window = Window(self.canvas, width=20, height=8, title='Window')
            Area(window, align='left', size=3)
            window.fill()
            self.canvas.set_focus(window)
        elif x == ord('5'):
            window = Window(self.canvas, width=20, height=20, title='Window')
            area = Area(window, align="left", size=10)
            Separator(window, align='left')
            area2 = Area(window, align="left", size=7)
            area.fill()
            area2.display('Some text to be displayed')
            self.canvas.set_focus(window)
        elif x == ord('6'):
            window = ButtonWindow(self.canvas, width=60, height=20, title='ButtonWindow')
            window.add_button(Button(window, 'd', 'default', action='action'))
            window.add_button(Button(window, 'w', 'warning', color=C_WARN, action='action'))
            window.add_button(Button(window, 'd', 'danger', color=C_DANGER, action='action'))
            window.add_button(Button(window, 'i', 'info', color=C_INFO, action='action'))
            window.add_button(OKButton(window))
            window.add_button(LoggerButton(window, text='To jest przykładowy log'))
            self.canvas.set_focus(window)

    def handle_focus_window(self, focused_window, x):
        if chr(x) in focused_window.keys:
            action = focused_window.keys[chr(x)]
            action()
        elif x == K_ESCAPE or x == K_ENTER:
            focused_window.destroy()
            self.canvas.set_focus(None)

    def handle_exit(self):
        window = TextWindow(self.canvas, width=30, height=6, title='Zakończenie gry')
        self.canvas.set_focus(window)
        window.add_button(OKButton(window))
        window.text.display('Granie zostanie ukończone.  Utracisz wszystkie postępy.')

        
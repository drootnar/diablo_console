import curses
from .views.windows import *
from .views.board import Canvas
from .views.buttons import Button, OKButton
from .const import *

__all__ = ['GameLoop', 'GameState']


class GameLoop:
    def __init__(self):
        self.canvas = Canvas()
        self.state = GameState()

    def run(self):
        x = None
        while True:
            x = self.canvas.input()
            focused_window = self.canvas.get_focus()
            if not focused_window:
                # focused on main screen
                if x == ord('1'):
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
                    area2.display('Przykładowy tekst')
                    self.canvas.set_focus(window)
                elif x == ord('6'):
                    window = ButtonWindow(self.canvas, width=60, height=20, title='ButtonWindow')
                    window.add_button(Button(window, 'd', 'default', action='action'))
                    window.add_button(Button(window, 'w', 'warning', color=C_WARN, action='action'))
                    window.add_button(Button(window, 'd', 'danger', color=C_DANGER, action='action'))
                    window.add_button(Button(window, 'i', 'info', color=C_INFO, action='action'))
                    window.add_button(OKButton(window))
                    self.canvas.set_focus(window)
                elif x == K_ESCAPE:
                    window = TextWindow(self.canvas, width=30, height=6, title='Zakończenie gry')
                    self.canvas.set_focus(window)
                    window.add_button(OKButton(window))
                    window.text.display('Granie zostanie ukończone.  Utracisz wszystkie postępy.')
                    break
            else:
                if chr(x) in focused_window.keys:
                    action = focused_window.keys[chr(x)]
                    action()
                elif x == K_ESCAPE:
                    focused_window.destroy()
                    self.canvas.set_focus(None)
            self.canvas.move(0, 0)
        self.canvas.close()

class GameState:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.points = [[(x % i) for i in range(1, 11)] for x in range(1, 12)]
        
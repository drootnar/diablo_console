from ..const import C_BUTTON, C_UNDERLINE, C_BOLD
from ..errors import ViewError

__all__ = ['Button', 'OKButton']


class Button:
    def __init__(self, window, key, name, *args, **kwargs):
        self.window = window
        self.key = key
        self.name = name
        self.color = kwargs.get('color', C_BUTTON)

    def action(self, *args, **kwargs):
        raise ViewError('Wrong button created')

    def render(self, y, x):
        if self.key.lower() in self.name.lower():
            place = self.name.lower().index(self.key.lower())
            self.window.obj.addstr(y, x, ' {} '.format(self.name), self.color)
            self.window.obj.addstr(y, x+place+1, self.key, self.color | C_UNDERLINE | C_BOLD)
            return len(self.name) + 2
        else:
            self.window.obj.addstr(y, x, ' {} {} '.format(self.key, self.name), self.color)
            self.window.obj.addstr(y, x+1, self.key, self.color | C_UNDERLINE | C_BOLD)
            return len(self.name) + 4


class OKButton(Button):
    def __init__(self, window):
        super(OKButton, self).__init__(
            window=window,
            key='o',
            name='OK',
        )

    def action(self, *args, **kwargs):
        self.window.destroy()
        self.window.canvas.set_focus(None)

import curses

K_ESCAPE = ord('q')

C_RED = curses.color_pair(1)
C_GREEN = curses.color_pair(2)
C_YELLOW = curses.color_pair(3)
C_BLUE = curses.color_pair(4)
C_MAGENTA = curses.color_pair(5)
C_CYAN = curses.color_pair(6)
C_WHITE = curses.color_pair(7)

C_FILL_RED = curses.color_pair(8)
C_FILL_GREEN = curses.color_pair(9)
C_FILL_YELLOW = curses.color_pair(10)
C_FILL_BLUE = curses.color_pair(11)
C_FILL_MAGENTA = curses.color_pair(12)
C_FILL_CYAN = curses.color_pair(13)
C_FILL_WHITE = curses.color_pair(14)

C_DANGER = curses.color_pair(15)
C_WARN = curses.color_pair(16)
C_OK = curses.color_pair(17)
C_INFO = curses.color_pair(18)
C_BUTTON = curses.color_pair(19)

C_BOLD = curses.A_BOLD
C_NORM = curses.A_NORMAL
C_UNDERLINE = curses.A_UNDERLINE
C_REVERSE = curses.A_REVERSE

VERSION = '0.1'
SIDE_PANEL_WIDTH = 30
LOGGER_HEIGHT = 3
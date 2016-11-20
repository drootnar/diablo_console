from curses import wrapper
import curses

from diablo_console.errors import GeneralDiabloConsoleError

def start_game(stdscr):
    curses.initscr()
    from diablo_console.controller import GameLoop
    from diablo_console.setup import setup
    stdscr.clear()
    try:
        setup()
        game = GameLoop()
        game.run()
    except GeneralDiabloConsoleError as e:
        pass
    stdscr.refresh()
    stdscr.getkey()

wrapper(start_game)
from curses import wrapper
import curses

def start_game(stdscr):
    curses.initscr()
    from diablo_console.controller import GameLoop
    from diablo_console.setup import setup
    stdscr.clear()
    setup()
    game = GameLoop()
    game.run()
    stdscr.refresh()
    stdscr.getkey()

wrapper(start_game)
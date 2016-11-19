from curses import wrapper

from diablo_console.controller import GameLoop

def start_game(stdscr):
    stdscr.clear()
    game = GameLoop()
    game.run()
    stdscr.refresh()
    stdscr.getkey()

wrapper(start_game)
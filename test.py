import curses
from curses import wrapper
import time

def main(stdscr):

    # stdscr.nodelay(True)

    row = 0
    col = 10

    # height = 25
    # width = 111









    # while True:

    #     stdscr.clear()
    #     #draws a char("a num 1") @ (0,10)
    #     stdscr.addstr(row, col,"1")

    #     stdscr.refresh()
        
    #     row += 1

    #     height, width = stdscr.getmaxyx()

    #     if row > height-1:
    #         row = 0
        


    #     time.sleep(0.1)


wrapper(main)
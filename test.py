import curses
from curses import wrapper
import time
import random

def rain_test(stdscr):

    curses.curs_set(0)
    stdscr.nodelay(True)

    # row = 0
    # col = []

    # height, width = stdscr.getmaxyx()

    current_row = 0
    col = []
    height, width = stdscr.getmaxyx()
    
    
    for i in range(width):
        col.append(random.randint(-height, -1)) 

    while True:
        
        stdscr.clear()

        for i, current_row in enumerate(col):
           
           if current_row >= 0 and current_row < 0:
               stdscr.addstr(current_row, i, "1")
               col[i] += 1

           if col[i] > height-1: 
                col[i] = 0


           

        stdscr.refresh()
        time.sleep(0.1)

wrapper(rain_test)
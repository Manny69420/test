import curses
from curses import wrapper
import time
import random

def rain_test(stdscr):

    curses.curs_set(0)
    stdscr.nodelay(True)


    current_row = 0
    col = []


    height, width = stdscr.getmaxyx()
    
    #sets a random row value to any new number drawn on the screen(it just makes the number go in different places)
    for i in range(width):
        col.append(random.randint(-height, -1)) 

    while True:
        
        stdscr.clear()


        for i, current_row in enumerate(col):
           
           if current_row >= 0 and current_row < height:
                
                #tells the program to do nothing when numbers are drawn below the height of the terminal 
                try:
                    stdscr.addstr(current_row, i, "1")  
                except curses.error:
                    pass
                 
           col[i] += 1 


           if col[i] > height-1: 
                col[i] = 0

        stdscr.refresh()
        time.sleep(0.1)

wrapper(rain_test)
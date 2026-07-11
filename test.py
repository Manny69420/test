import curses
from curses import wrapper
import time
import random

def rain_test(stdscr):

    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)


    
    current_row = 0
    col = []
    speed = []
    frame_ctr = 0
    char = ["1", "0"]
    step = 0

    height, width = stdscr.getmaxyx()
    
    #fills our col list with random values (how we get the different character positions)
    for i in range(width):
        col.append(random.randint(-height, -1)) 

    for j in range(width):
        speed.append(random.randint(1, 3))


    while True:
        stdscr.clear()

        frame_ctr += 1

        for i, current_row in enumerate(col):
            
           if current_row >= 0 and current_row < height:
                
                #tells the program to do nothing when numbers are drawn below the height of the terminal 
                try:
                    #draws the "head" of each strand
                    stdscr.addstr(current_row, i, random.choice(char), curses.color_pair(1))

                    #takes care of the the rest of the strand so wtvs behind the head(the tail)
                    for step in range(1,5):

                        stdscr.addstr(current_row - step, i, random.choice(char), curses.A_DIM +curses.color_pair(1))

                except curses.error:
                    pass


           if frame_ctr % speed[i] == 0:
                col[i] += 1


           if col[i] > height-1: 
                col[i] = random.randint(-height, -1)

        stdscr.refresh()
        time.sleep(0.02)

wrapper(rain_test)
#!/usr/bin/env python

import curses
from curses import error, wrapper
from inspect import Traceback
import time
import argparse
import math

'''
parser = argparse.ArgumentParser(description='Do a typing test!')
parser.add_argument('--mode', help='set mode of the typing test')
'''
toprintout = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut laboreetdolore magna aliqua. Lorem sed risus ultricies tristique. Ut sem nulla pharetra diam sit amet nisl suscipit.'
x = 0

def main(stdscr):
    global x
    stdscr.clear()
    stdscr.addstr(0, 0, "ned's typing test")
    typing = curses.newpad(100,100)
    border = curses.newwin(102, 102, 2, 2)
    border.border('|', '|', '-', '-', '+', '+', '+', '+')
    border.addstr('Start Typing!')
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)

    reg = curses.color_pair(1)

    typing.addstr(toprintout)
    w2 = 150
    w1 = 5
    wt = w2 - w1
    stdscr.refresh()
    r = 0
    typing.refresh(0, 0, 3, w1, 5, w2)

    while x != len(toprintout):
        result = typing.getch()
        if result == 27:
            break
        elif result == 127 and len(toprintout) >= 1:
            x -= 1
        elif result != 127 and result == ord(toprintout[x]):
            x += 1
        
        '''    
        if x%145==0:
            r += 1
            typing.refresh(r, 0, 3, 5, 5, 150)
        '''
        typing.clear()
        #typingwin.addstr(0, 0, curses.keyname(result))
        typing.addstr(0, 0, toprintout[:x], reg)
        print("{}, {}".format(x//100, x%100))
        typing.addstr(x//100, x%100, toprintout[x:])
        '''
        if x//100 == 1:
            typing.addstr(x//100, x-(100 * x//100), toprintout[x:])
        else:
            typing.addstr(0, x, toprintout[x:])
        '''
        stdscr.addstr(0, 20, 'col: {}, row: {}'.format(x//100, x%100))
        stdscr.addstr(0, 40, "current WPM: " + str((x / 5) / ((time.time() - timenow)/60)))
        stdscr.refresh()
        typing.refresh(x//100, 0, 3, w1, 5, w2)
    

#print(curses.get_tabsize())
timenow = time.time()
try:
    wrapper(main)
except:
    print("Could not run program, try resizing your terminal to at least 105x17")
print('Finished! Your gross WPM is {}'.format((x / 5 ) / ((time.time() - timenow)/60)))


'''
import pathlib

p = pathlib.Path(__file__)

print(p.parent)
GODSEND
'''
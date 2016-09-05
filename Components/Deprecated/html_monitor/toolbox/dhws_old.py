import os
import time
import sys
from Modules import operator_scheduler
if __name__ == "__main__":
    arg = (sys.argv)
    #11 for vessell, 13 for leviathan
    commands = ["from pio import pio\np = pio()", "p.o(True, 11)", "p.o(False, 11, True)"]
    if len(arg) != 1:
        if len(arg) == 2:
            if arg[1] == "wake_up":
                arguments =  [1, 0, 1, 1]
            if arg[1] == "shutdown":
                arguments = [1, 0, 5, 1]
        elif len(arg) == 4:
            if arg[2] == "-t":
                t = int(arg[3])
                arguments = [1, t, 5, 1]

        operator_scheduler.clock(commands, arguments)
    else:
        print "usage: python dhws_old.py [wake_up/shutdown] [-t x]"

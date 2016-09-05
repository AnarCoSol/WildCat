import os
import time
import sys
import threading

from Modules.operator_scheduler_new import clock
from Modules.Text_manipulator import Text_manipulator
#Power Line On/Off
#Version = 'recursive' 07/03/16
#raw version static, need more flexibility and reusability

class Sub_thread(threading.Thread):
    def __init__(self, name = str(), program = str(), argvs = str()):
        threading.Thread.__init__(self)
        self.name = name
        self.argvs = argvs
        self.program = program
    def run(self):
        os.system(self.program + " " +  self.argvs)
        exit()

if __name__ == "__main__":
    
    arg = (sys.argv)
    if len(arg) != 1:
        if arg[1] == "on":
            state = "True"
            clean = "False"
            
        if arg[1] == "off":
            state = "False"
            clean = "True"

        pin = "15"

        cmd = ("from pio import pio" + "\n" +
               "p = pio()" + "\n" +
               "p.o("  + state + "," + pin + "," + clean + ")"
               )

        clock(
            command = cmd,
            argvs = [range(1), 1, 0],
            txt = list(),
            meta = list()
            )
    else:
        print "usage: python " + __file__  + " [on/off]"

#clock(command = str(), argvs = list(), txt = list(), meta = list())

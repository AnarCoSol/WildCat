import os
import time
import sys
import threading

from Modules.operator_scheduler_new import clock
from Modules.Text_manipulator import Text_manipulator


#Version = 'recursive' 07/03/16
#Dark Hurd Wake_up/Shutdown
def enum(string = str(), split_char = ","):
    tokens = string.split(split_char)
    for t in tokens:
        if t[-4:] == ".txt":
            tm = Text_manipulator()
            raw_string = tm.Read()
            tokens = tokens + enum(raw_string, "\n")
            
    return tokens

def dictionarize(l = list(), d = dict()):
    for x in l:
        y = x.split(":")
        if len(y) == 2:
            d[y[0]] = y[1]
            
        elif len(y) == 1:
            d[y[0]] = None
    return d

def dict_comparize(d1 = dict(), d2 = dict()):
    ("""second one must be the older""")
    d3 = dict()
    for k in d1.keys():
        if d1[k]:
            d3[k] = d1[k]
        else:
            if d2.has_key(k):
                d3[k] = d2[k]

    return d3

class Sub_thread(threading.Thread):
    def __init__(self, name = str(), program = str(), argvs = str()):
        threading.Thread.__init__(self)
        self.name = name
        self.argvs = argvs
        self.program = program
    def run(self):
        os.system(self.program + " " +  self.argvs)
        exit()
        
def plof_run(plof_trigger = str(), plof_path = str()):
    try:
        sub_th = Sub_thread( name = "plof", program = plof_path, argvs = plof_trigger)
        sub_th.start()
        sub_th.join()
    except:
        raise

def getScriptPath():
        return os.path.dirname(__file__)

if __name__ == "__main__":
    
    arg = (sys.argv)
    #it can be stored in a database or in a text file
    nodes = {"leviathan": 13, "vessell": 11} # <- it can be retrieved with SQL_agent in a database where saved key:value
    
    if len(arg) != 1:
        t = int()
        if arg.count("-t"):
            try:
                t = int(arg[arg.index("-t") + 1])
            except:
                raise
                #print "problem with -t x secs"
        t_status = dict()
        if arg[1] == "wake_up":
            t_status = 1
            
        if arg[1] == "shutdown":
            t_status = 5
            
        if arg.count("-n"):                               
            nodes = dict_comparize(dictionarize(enum(str(arg[arg.index("-n") + 1]), ",")), nodes)
            
        plof_trigger = str()
        
        if arg.count("-pl"):
            if t_status == 1:
                plof_trigger = "on"
            elif t_status == 5:
                plof_trigger = "off"


            
            
            
        print nodes #
            
                    
        if arg.count("-m"):
            mode = str(arg[arg.index("-m") + 1])
        else:
            mode = "parallel"

        if plof_trigger == "on":
            plof_run(plof_trigger, "python "  + getScriptPath() + "/plof.py")
            
        if mode == "series":
            
            clock(command = ('clock(command = ' + '"' +
                             
                                 't = (' + str(t_status) + ' if i == True else 0)' + '\\n' +
                                 'print t' + '\\n' +
                                 'clock(command = ' + '\'' +
                             
                                     'from pio import pio' + '\\\\n' +
                                     'p = pio()' + '\\\\n' +
                                     'x = (-3 if meta[-2] == True else -5)' + '\\\\n' +
                                     'p.o(meta[-2], int(meta[0].get(meta[x])), not meta[-2])' + '\'' +
                             
                                 ',argvs = [range(1),0,t], meta = meta)' + '"' +
                             
                             ',argvs = [[True,False],0,0], meta = meta)'),
                  
                  argvs = [nodes,0,0], meta = [nodes])
            
        else:
            for node in nodes:
                sub_th = Sub_thread( name = str(node), program = "python " + getScriptPath() + "/dhws.py", argvs = arg[1] + " -n " + str(node) + ":" + str(nodes[node]) + " -m series")
                sub_th.start()
                sub_th.join()
                
        if plof_trigger == "off":
            plof_run(plof_trigger)
    else:
        print ("usage: python " + __file__ +  """ [wake_up/shutdown] [-t x] -n ['node/node1,node2,../file'] -m [PARALLEL/series] -pl

                          ====== Options available ======
                        -n [] <- nodes to wake_up/shutdown
                        -m [] <- mode to wake_up/shutdown the nodes
                        -pl   <- power_on/_off the power_line
                        """)

#clock(command = 'clock(command = "t = (' + str(t_status) + ' if i == True else 0)\\nprint t\\nclock(command = \'from pio import pio\\\\np = pio()\\\\nx = (-3 if meta[-2] == True else -5)\\\\np.o(meta[-2], meta[0].get(meta[x]), not meta[-2])\',argvs = [range(1),0,t], meta = meta)",argvs = [[True,False],0,0], meta = meta)', argvs = [nodes,0,0], meta = [nodes])

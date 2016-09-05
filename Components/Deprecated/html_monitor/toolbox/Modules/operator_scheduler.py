import os
import time
import threading
#from pio import pio #modded
#p = pio()
class c_thread(threading.Thread):
    def __init__(self,x):
        threading.Thread.__init__(self)
        self.x = x
        self.status = -1
    def run(self,process):
        try:
            exec process in globals(), locals()
        except:
            print "thread error"
            

#dis = 24*(60**2) as "day in secs"
def format_c_time():
    return int(((int(time.ctime()[-13:-11]))*(60**2)) +
                ((int(time.ctime()[-10:-8]))*60) +
               (int(time.ctime()[-7:-5])))
def format_reply(reply):
    return int(((int(reply[0:2])*24*(60**2)) +
                       ((int(reply[3:5]))*(60**2)) +
                      ((int(reply[6:8]))*60) +
                       (int(reply[9:11])))) #format reply in secs
def clock(commands = list(), argvs = list(), txt = list()):
    if commands == list():
	commands.append("print 'command 0'")
        commands.append("print 'command 1'")
        commands.append("print 'command 2'")
    if len(txt) != 5:
        print "txt list not passed"
        def err_exec(command):
            return str("error executing " + str(command))
        
        txt = ["repeat for [x times]: ",
               "process start [x secs] from now: ",
               "first signal duration [x secs]: ",
               "second signal duration [x secs]: ",
                "err_exec"
               ]
        print "set default"
        
    if argvs == list():
        repeat_for = input(txt[0])
        from_now = input(txt[1])
        first_pause = input(txt[2])
        second_pause = input(txt[3])
    else:
        repeat_for = argvs[0]
        from_now = argvs[1]
        first_pause = argvs[2]
        second_pause = argvs[3]

    try:
        exec str(commands[0]) in globals(), locals() #importing modules
    except:
        if len(txt) != 4: txt[4] = err_exec(commands[0])
        print txt[4]
        
    print "process started at " + str(time.ctime()) #it should be customisable
    print "sleeping for " + str(from_now) + " secs"
    time.sleep(from_now)
    for i in range(repeat_for):
        try:
            exec str(commands[1]) in globals(), locals()
        except:
            if len(txt) != 4: txt[4] = err_exec(commands[1])
            print txt[4]
        time.sleep(first_pause)
        try:
            exec str(commands[2]) in globals(), locals()
        except:
            if len(txt) != 4: txt[4] = err_exec(commands[2])
            print txt[4]
        time.sleep(second_pause)
        print str(i +1) + " of " + str(repeat_for) + " " + str(time.ctime())
if __name__ == "__main__":
    print "this is just an example: "
    clock()

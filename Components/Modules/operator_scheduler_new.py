import os
import time
import threading
#Version = "recursive" 07/03/16
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


def clock(command = str(), argvs = list(), txt = list(), meta = list()): # <--meta needed
    if command == str():
        command = "print 'command 1'"
    if len(txt) != 5:
        print "txt list not passed"
        def err_exec(command):
            return str("error executing " + str(command))
        
        txt = ["repeat first command for [a list]: ",
               "process start [x secs] from now: ",
               "first signal duration [x secs]: ",
               "second signal duration [x secs]: ",
                "err_exec"
               ]
        #print "set default"
        
    if argvs == list():
        repeat_for = range(input(txt[0]))
        from_now = input(txt[1])
        pause = input(txt[2])
    else:
        repeat_for = argvs[0]
        from_now = argvs[1]
        pause = argvs[2]

    print "process started at " + str(time.ctime()) #it should be customisable (with exec)

    print "sleeping for " + str(from_now) + " secs"

    time.sleep(from_now)
    
    for i in repeat_for:
        meta.append(i)
        #print "i: " + str(i)
        #print "meta: " + str(meta)
        #print "command: " + str(command)
        try:
            exec str(command) in globals(), locals()
        except:
            raise
            #if len(txt) != 4: txt[-1] = err_exec(command)
            #print txt[-1]

        print "pause for " + str(pause) + " secs"
        time.sleep(pause)
        
if __name__ == "__main__":
    print "this is just an example: "
    clock()

import os
import sys

from toolbox.Modules.Text_manipulator import Text_manipulator

if __name__ == "__main__":
    argvs = sys.argv
    tm = Text_manipulator()
    if len(argvs) != 1:
        if len(argvs) == 2:
            if argvs[1] == "write":
                while True:
                    try:
                        tm.Write_as_output("in.txt", raw_input("> "))
                    except KeyboardInterrupt:
                        break
                    except:
                        raise
            elif argvs[1] == "read":
                while True:
                    try:
                        tm.Read_and_print("in.txt")
                    except KeyboardInterrupt:
                        break
                    except:
                        raise
            else:
                pass #it can be the case of read and write at the same time or original child.interact()
            
                    
    else:
        print "usage: python Trinity.py [read/write]"

import os
import sys

from Modules.Text_manipulator import Text_manipulator

class Trinity():
    def __init__(self):
        self.tm = Text_manipulator()

    def man_in(self,in_file = str()):
        while True:
            try:
                self.tm.Write_as_output(in_file, raw_input("> "))
            except KeyboardInterrupt:
                break
            except:
                raise

    def semi_in(self, in_file = str()):
        pass

    def auto_in(self, in_file = str()):
        pass

    def ai_in(self, in_file = str()):
        pass
    
    def man_out(self, out_file = str()):
        while True:
            try:
                self.tm.Read_and_print("in.txt")
            except KeyboardInterrupt:
                break
            except:
                raise
        
if __name__ == "__main__":
    argvs = sys.argv
    if len(argvs) != 1:
        trinity = Trinity()
        
        if len(argvs) == 2:
            if argvs[1] == "write":
                trinity.man_in()
                
            elif argvs[1] == "read":
                trinity.man_out()
            else:
                pass #it can be the case of read and write at the same time or original child.interact()
            
                    
    else:
        print "usage: python Trinity.py [read/write]"

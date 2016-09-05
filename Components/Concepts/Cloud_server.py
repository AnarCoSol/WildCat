import os
import sys

from Modules.File_manager import Cloud_manager

from Modules.Thread_launcher import Thread_launcher

from Modules.Matrix import Matrix_spawner

class Cloud_server():
    def __init__(self, dirs = list()):
        self.cm = Cloud_manager()
        
        self.dirs = dirs

    def pull(self):
        pass

    def push(self):
        pass

    def observer(self):
        for d in dirs:

        return
            
    
    def start(self):

        while True:
            pass
            

if __name__ == "__main__":
    argvs = sys.argv

    if len(argvs) != 1:
        pass
    else:
        print "usage: python " + __file__  + " start"

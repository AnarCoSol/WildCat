import os
import sys

from Modules.File_manager import Cloud_manager
#recursive mode? if dir in a list: recursive

if __name__ == "__main__":
    argvs = sys.argv

    if len(argvs) != 1:
        cm = Cloud_manager()

        path = argvs[1]
        while True:
            result = cm.watch_dir(path, "r")
            
            if result:
                print "changed: " + path
            else:
                print "something has gone wrong"
        

    else:
        print "usage: python " + __file__  + " dir"

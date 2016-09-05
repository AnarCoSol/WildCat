#changelogs:
#
#notes:
#maybe it can be move in Modules
#todo:
#


import sys
#Op core modules
from Modules.Messenger import Messenger
class M():
    def __init__(self):
        self.send = Messenger.send
if __name__ == "__main__":
    arg = sys.argv
    m = M()
    if len(arg) == 1:
        print "usage: python " + __file__  + " [push/pull] 'file1,[file_list.txt],file3,...'"
    elif len(arg) == 2:
        print "files omitted"
    else:
        try:
            #if [file_list.txt]: for x in line: sys.argv.append(x)
            #m.send(blablabla, sys.argv[x:])
            pass
        except:
            raise

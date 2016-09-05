import sys
import os

from Modules.Formatter import Formatter as formatter

class Formatter():

    def __init__(self):
        pass

    def elaboration(self, i = str(), m = str()):

        if i.count(m):
            
            o =  i.replace(m, str())
            return o

    def server(self, mode = str(), mask_in = str(), mask_out = str()):
        
        while True:
            
            o = self.elaboration(i = raw_input(mask_out), m = mask_in)

            if o:
                print o
            
        

if __name__ == "__main__":
    argvs = sys.argv

    if len(argvs) != 1:
        if argvs.count("-mi"):

            m_in = argvs[argvs.index("-mi") + 1 ]

        if argvs.count("-mo"):

            m_out = argvs[argvs.index("-mo") + 1]

        f = Formatter()

        f.server(mask_in = m_in, mask_out = m_out)
        
            

    else:
        print "usage: python " + __file__ + "-mi [mask_in] -mo [mask_out]"
    

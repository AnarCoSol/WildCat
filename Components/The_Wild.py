import sys
import os

from Cat import __file__ as Cat_path
import __init__
slash = "/" #sketchy
__file__ = os.path.dirname(__init__.__file__) + slash +  __file__.split(slash)[-1]

__usage__ = "python " + __file__  + " [start]"

script_name = os.path.basename(__file__)[:-3]

script_path = os.path.dirname(__file__)
if script_path == str():
    data_path = "Data"
else:
    data_path = script_path + "/Data"

if __name__ == "__main__":
    argvs = sys.argv
 
    if len(argvs) != 1:

        if argvs[1] == "start":

            if len(argvs) != 1: #2

                command = ("python " + Cat_path + " start " +
                           "-c 'python "+ Cat_path + " server' " +
                           "-i " + data_path + "/" + "IDebug.txt " +
                           "-o " + data_path + "/" + "CatDebug.txt " +
                           "-m 'io cat' " +
                           "-mi " + data_path + "/" + "Cat_mask_in.txt " +
                           "-mo " + data_path + "/" + "Cat_mask_out.txt " +
                           "-echo " + "False"
                           )
                print "Command launched: " + str(command)
                
                os.system(command)
                

    else:
        print ("""
_________________________________________________________________________

program: %s
directory: %s
credits: %s
coded by: %s
license: %s
usage: %s
_________________________________________________________________________

""" % (
        os.path.basename(__file__),
        os.path.dirname(__file__),
        __init__.__credits__,
        __init__.__author__,
        __init__.__license__,
        __usage__
        ))

#the wild launch cat and send to it a list of command to boot the core of
# a program
#then maybe can ask (as Cat) for run other programs
#and then run a monitor console maybe

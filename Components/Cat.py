import os
import sys

from Modules.Daemon import Daemon

from Modules.Thread_launcher import Thread_launcher
from Modules.Matrix import Matrix_spawner
from Modules.Matrix import __file__ as matrix_path

#or Importer(Matrix_spawner)
import __init__
slash = "/" #sketchy
__file__ = os.path.dirname(__init__.__file__) + slash +  __file__.split(slash)[-1]
script_path = os.path.dirname(__file__)

__usage__ = ("""python " + __file__  + " [start/server]"
    start options:
        -c [command]
        -i [in_file]
        -o [out_file]
        -m [mode]
        -mi [mask_in]
        -mo [mask_out]
        -echo [True/False]
        
    """)

def Matrix_run(a = list()):

    if len(a) == 4:
        
        m.matrix_run(command = a[0], out_f = a[1], in_f = a[2], mode = a[3])


        

if __name__ == "__main__":
    argvs = sys.argv

    if len(argvs) != 1:
        
        if argvs[1] == "server":
            try:
                m = Matrix_spawner()
                
                while True:
                    get_in = [
                        "command: ",
                        "input file: ",
                        "output file: ",
                        "mode: ",
                        "mask_in: ",
                        "mask_out: ",
                        "echo: "
                        ]
                    
                    arg_in = list()
                    
                    for g in get_in:
                    
                        arg_in.append(raw_input(g))

                    command = ("python " + matrix_path + " matrix_run " +
                               "-c " + arg_in[0] + " " +
                               "-i " + arg_in[1] + " " +
                               "-o " + arg_in[2] + " " +
                               "-m " + arg_in[3] + " " +
                               "-mi " + arg_in[4] + " " +
                               "-mo " + arg_in[5] + " " +
                               "-echo " + arg_in[6] + " &"
                               )

                    os.system(command)
##                    
##                    d = Daemon("/tmp/" + program_name + ".pid", func = Matrix_run, argvs = arg_in )
##
##                    d.start()
##                    print 'a'
            except KeyboardInterrupt:
                pass
            
            except:
                raise


        elif argvs[1] == "start":
                
            if len(argvs) != 2:

                if argvs.count("-c"):
                    command = argvs[argvs.index("-c") + 1]

                if argvs.count("-i"):
                    in_file = argvs[argvs.index("-i") + 1]
                else:
                    in_file = "in.txt"

                if argvs.count("-o"):
                    out_file = argvs[argvs.index("-o") + 1]
                else:
                    out_file = "out.txt"

                if argvs.count("-m"):
                    mode = argvs[argvs.index("-m") + 1]
                else:
                    mode = "io file"

                if argvs.count("-mi"):
                    mask_in = argvs[argvs.index("-mi") + 1]
                else:
                    mask_in = "mask_in.txt"

                if argvs.count("-mo"):
                    mask_out = argvs[argvs.index("-mo") + 1]
                else:
                    mask_out = "mask_out.txt"

                if argvs.count("-echo"):
                    echo = argvs[argvs.index("-echo") + 1]
                else:
                    echo = "True"
                    

                def stringfy( str_in = str()):
                    if str_in.count(" "):
                        return "'" + str_in + "'"

                    else:
                        return str_in
                
                command = ("python " + matrix_path + " matrix_run " +
                           "-c " + stringfy(command) + " " +
                           "-i " + stringfy(in_file) + " " +
                           "-o " + stringfy(out_file) + " " +
                           "-m " + stringfy(mode) + " " + 
                           "-mi " + stringfy(mask_in) + " " +
                           "-mo " + stringfy(mask_out) + " " +
                           "-echo " + stringfy(echo) + " &"
                           )

                #print command
                

                os.system(command)
                
            else:
                print "usage: python " + __file__  + " [start/server]"
                         

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
        


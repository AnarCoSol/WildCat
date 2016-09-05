import os
import sys
import subprocess
import pty

import pexpect_hacked as pexpect

import __init__#or itself as import mail_client.__file__
slash = "/" #sketchy
__file__ = os.path.dirname(__init__.__file__) + slash +  __file__.split(slash)[-1]

__usage__ = ("python " + __file__  + """[pty/matrix/sub/matrix_run] [argv]
Arguments:

    matrix/matrix_run: -c [command] -i [in_file] -o [out_file] -m [mode] -mi [mask_in] -mo [mask_out] -fi [input filter] -fo [output filter] -echo [True/False]
        [mode] = 'i file'/'o file'/'io file'/'io direct'/'io inverted'/'io cat'
        
    pty/sub: [argvs]
""")

from Text_manipulator import Text_manipulator
# if some problem with lines not meta-data data.split ecc
class Matrix_filter():

    def __init__(self, mask_in = str(), mask_out = str()):

        self.mask_in = mask_in
        self.mask_out = mask_out
        self.tm = Text_manipulator()
        
    def filter_in(self, i = str()):
        
        try:
            raw = self.tm.Read(self.mask_in).split("\n")
            
            #self.tm.Write_add("debug.txt", i) for debugging
            
            if i.count("|"):
                data = i[i.index("|") + 1 :]
            else:
                return None

            meta_data = i[:i.index("|")]

            for token in raw:
                
                if token != str() and token != " ":

                    if meta_data.count(token):
                        
                        return data

            return None

        except:
            raise    

    def filter_out(self, i = str()):
        # split the meta data with the data as: "meta-data | data"
        try:
            raw = self.tm.Read(self.mask_out).split("\n")
            meta_data = str()
            
            for token in raw:

                if token != str() and token != " ":

                    meta_data += (token + " ")

                    

            return (meta_data[:-1] + "|" + i)

        except:
            raise

                    
    
class Matrix_spawner():
    def __init__(self):
        self.processes = list()

    def getScriptPath(self):
        return os.path.dirname(__file__)

    def spawn_sub(self, args_list = list(), sh = False, silent = False):
        
        if silent:
            
            devnull = open(os.devnull, 'wb')
            
            stde = devnull
            stdo = devnull
            stdi = devnull
            
            self.processes.append(subprocess.Popen(args_list, shell = sh, stdout = stdo, stderr = stde))

        else:
            self.processes.append(subprocess.Popen(args_list, shell = sh))
            
        return self.processes[-1]

    def spawn_pty(self, args_list = list()):
                
        pty.spawn(args_list)

    def kill_by_pid(self, pid = str()):
        for p in self.processes:
            if p.pid == int(pid):
                
                p.kill
                return str(p.pid) + " killed"
            
        return "process " + pid + " not found"
    
    def kill_all(self):
        for proc in self.processes:
            proc.kill
            print str(proc.pid) + ": killed"

    def matrix_spawn(self, command = str(), in_f = str(), out_f = str(), mode = str(), out_filter = None, in_filter = None, echo = "True"):

        if echo == "False":
            echo = False
        elif echo == "True":
            echo = True
        
        child = pexpect.spawn(command, in_file = in_f, out_file = out_f, mode = mode, echo = echo)

        child.interact(output_filter = out_filter, input_filter = in_filter)

    def matrix_run(self, command = str(), in_f = str(), out_f = str(), mode = str(), scriptpath = __file__, m_in = str(), m_out = str(), out_filter = None, in_filter = None, echo = "True"):
        args_l = ["python", scriptpath,
                                    "pty",
                                        "python", scriptpath,
                                            "matrix",
                                                "-c", command,
                                                "-i", in_f,
                                                "-o", out_f,
                                                "-m", mode,
                                                "-echo", echo,
                  ]
        
        if out_filter:
            args_l = args_l + ["-fo", out_filter]

        if in_filter:
            args_l = args_l + ["-fi", in_filter]

        if m_in:
            args_l = args_l + ["-mi", m_in]

        if m_out:
            args_l = args_l + ["-mo", m_out]
            
            
        self.spawn_sub(args_list = args_l, silent = True)

if __name__ == "__main__":
    
    argvs = sys.argv
  
    if len(argvs) != 1:
        matrix_spawner = Matrix_spawner()
        
        if argvs[1] == "pty":
            matrix_spawner.spawn_pty(args_list = argvs[2:])

        elif argvs[1] == "sub":
            matrix_spawner.spawn_sub(args_list = argvs[2:])

        else:

            if argvs.count("-c"):
                c = argvs[argvs.index("-c") + 1]

            if argvs.count("-i"):
                i = argvs[argvs.index("-i") + 1]
                
            if argvs.count("-o"):
                o = argvs[argvs.index("-o") + 1]
                
            if argvs.count("-m"):
                m = argvs[ argvs.index("-m") + 1]

            if argvs.count("-mi"):
                mask_in = argvs[argvs.index("-mi") + 1]
            else:
                mask_in = None

            if argvs.count("-mo"):
                mask_out = argvs[argvs.index("-mo") + 1]
            else:
                mask_out = None


            if argvs.count("-fi"):
                pass
            else:
                fi = None

            if argvs.count("-fo"):
                pass
            else:
                fo = None

            if argvs.count("-echo"):
                echo = argvs[argvs.index("-echo") + 1]
            else:
                echo = "True"

            if not fo and not fi and mask_in and mask_out:

                try:

                    matrix_filter = Matrix_filter(mask_in = mask_in, mask_out = mask_out)

                    fi = matrix_filter.filter_in

                    fo = matrix_filter.filter_out

                except:
                    raise

                

            if argvs[1] == "matrix":
                
                matrix_spawner.matrix_spawn(command = c, in_f = i, out_f = o, mode = m, out_filter = fo,  in_filter = fi, echo = echo)

            elif argvs[1] == "matrix_run":
                
                matrix_spawner.matrix_run(command = c, in_f = i, out_f = o, mode = m, scriptpath = __file__, m_in = mask_in, m_out = mask_out, echo = echo)#out_filter = fo, in_filter = fi)
            
            
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


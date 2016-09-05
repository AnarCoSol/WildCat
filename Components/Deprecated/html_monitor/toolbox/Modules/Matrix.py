import os
import sys
import subprocess
import pty

import pexpect_hacked as pexpect
import Matrix

class Matrix_spawner():
    def __init__(self):
        self.processes = list()

    def getScriptPath(self):
        return os.path.dirname(os.path.realpath(sys.argv[0]))

    def spawn_sub(self, args_list = list(), sh = False, stdo = None, stde = None):
        devnull = open(os.devnull, 'wb')
        if not stde:
            stde = devnull
        if not stdo:
            stdo = devnull
            
            
        self.processes.append(subprocess.Popen(args_list, shell = sh, stdout = stdo, stderr = stde))
        return self.processes[-1]

    def spawn_pty(self, args_list = list()):
        pty.spawn(args_list)

    def kill_by_pid(self):
        self.p.kill
        return str(self.p.pid) + " killed"
    def kill_all(self):
        for proc in self.processes:
            proc.kill
            print str(proc.pid) + ": killed"

    def matrix_spawn(self, command = str(), in_f = str(), out_f = str(), out_filter = None, in_filter = None):
        child = pexpect.spawn(command, in_file = in_f, out_file = out_f)
        child.interact(output_filter = out_filter, input_filter = in_filter)

    def matrix_run(self, command = str(), in_f = str(), out_f = str(), scriptpath = os.path.dirname(Matrix.__file__)):
        scriptname = scriptpath + "/Matrix.py"
        self.spawn_sub(args_list = ["python", scriptname,
                                    "pty",
                                        "python", scriptname,
                                            "matrix",
                                                command, in_f, out_f])

if __name__ == "__main__":
    argvs = sys.argv
    if len(argvs) != 1:
        m = Matrix_spawner()
        
        if argvs[1] == "pty":
            m.spawn_pty(args_list = argvs[2:])

        if argvs[1] == "matrix":
            m.matrix_spawn(command = argvs[2], in_f = argvs[3], out_f = argvs[4])

        if argvs[1] == "sub":
            m.spawn_sub(args_list = argvs[2:])
        if argvs[1] == "matrix_run":
            m.matrix_run(command = argvs[2], in_f = argvs[3], out_f = argvs[4])
            
            
    else:
        print "usage: Matrix.py [pty/matrix/sub/matrix_run]"


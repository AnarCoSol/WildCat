import os
import sys

from Modules.Matrix import Matrix_spawner

script_path = os.path.dirname(__file__)

if __name__ == "__main__":
    argvs = sys.argv

    if len(argvs) != 1:
        try:
            m = Matrix_spawner()
            scripts = ["watch_dir.py", "watch_file.py 'echo files changed'"]

            for script in scripts:
                m.matrix_run(command = "python " +
                             script_path +
                             "/" + script + " " +
                             argvs[1], out_f = argvs[2], in_f = "in.txt",
                             mode = "o file")
        except:
            raise

        while True:
            pass
        
    else:
        print "usage: python " + __file__  + " [dirname] [out_file]"

#it can use only The Wild/Cat to implement the watcher, running the two (
# watch_dir and watch_file) as Daemons

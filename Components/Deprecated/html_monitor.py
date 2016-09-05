import os
import subprocess
import time
import sys

import atexit

from toolbox.Modules.Matrix import Matrix_spawner
from toolbox.Modules.status_bar import Status_bar
from toolbox.Modules.Text_manipulator import Text_manipulator

#it works, but some little bugs in reading/writing
#it maybe launch a formatter server that read from out.txt and write on monitor_text.html
#formatting data with a mask_file.txt. then index.html can contain more than one mon_text,
#permitting to get a multitaskin style. app (hird) must can be stop by html gui (button in index.html ad mon_text.html)


if __name__ == "__main__":
    argvs = sys.argv
    script_path = os.path.dirname(__file__)
    s_bar = Status_bar()
    
    if len(argvs) != 1:
        try:
            m = Matrix_spawner()
            tm = Text_manipulator()
            apps = [["python", "Http_server.py"],["python", script_path + "/toolbox/Modules/Formatter.py", "out.txt", "out.html"]]
            tm.Write_new(script_path + "/" +  "monitor_text.html", "")
            tm.Write_new(script_path + "/" + "in.txt", "auto cleanded\n")
            
            for app in apps:
                m.spawn_sub(args_list = app)
            
            port = str()
            while True:
                raw = tm.Read(script_path + "/port.txt").split("\n")
                for line in raw:
                    
                    if line != "":
                        port = line
                        print "port: " + port
                        print "url: " + script_path + "/toolbox/web_browser.py", "-u","http://localhost:" + port
                        
                        m.spawn_sub(args_list = ["python", script_path + "/toolbox/web_browser.py", "-u","http://localhost:" + port])
                        break
                if port != str():
                
                    tm.Write_new(script_path + "/port.txt", "")
                    break
                        
                

            m.matrix_run(command = argvs[1], in_f = script_path + "/in.txt", out_f = script_path + "/out.txt")


            try:
                tm.silent = True
                c = tm.Read_as_input(script_path + "/kill.txt")
                print c
                d = 2 + "a"
                #s_bar.input_timeout("\n...", 5)
            except:
                raise
            
        except:
            print "exiting"
            m.kill_all
            #atexit.register(m.kill_all)
            exit()
        
    else:
        print "usage: python " + __file__  + " [command] [input_file] [output_file]"

    
    

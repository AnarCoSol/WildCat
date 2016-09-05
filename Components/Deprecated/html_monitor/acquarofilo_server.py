import os
import acquarofilo_server

script_path = os.path.dirname(acquarofilo_server.__file__)
os.system("python " + script_path + "/" + "html_monitor.py 'python " + script_path + "/toolbox/" + "acquarofilo.py' in.txt out.txt")


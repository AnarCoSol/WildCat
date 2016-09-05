#acquarofilo
import os
import time
#from pio import pio #python rpi gpio
import Modules.operator_scheduler as operator_scheduler
if __name__ == "__main__":
    choice = raw_input("stai utilizzando un raspberry, un android o il jack [rpi/android/jack]? ")
    if choice == "rpi":
        module = "from pio import pio" + "\n" + "p = pio()"
        commands = [module, "p.o(True, 11)", "p.o(False, 11, True)"]
    if choice == "jack":
        module = "from audio import AudioFile" + "\n" + "a = AudioFile('sine.wav')"
        commands = [module, "a = AudioFile('sine.wav')\na.playf(2)", "a.close()"]
        
    if choice == "android":
        module = "from paio import android_GPIO"
        commands = [module, "a = android_GPIO()\na.o(state = '1')","a.o(state = '0')"]

    txt = ["quante volte vuoi dare il cibo ai pesci? ",
           "tra quanto tempo (a partire da ora) vuoi far partire il processo? " +
           " scrivilo in secondi, es. 24 ore = 24*(60**2) ",
           "ogni quanto tempo somministrare il cibo ai pesci? scrivilo in secondi "
           ]
    
    a = raw_input(txt[0])
    b = raw_input(txt[1])
    c = raw_input(txt[2])
    
    arguments = [int(a),int(b), 5, int(c)]
    operator_scheduler.clock(commands, arguments)
    exit()
    
    

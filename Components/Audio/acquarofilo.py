#acquarofilo
import os
import time
#from pio import pio #python rpi gpio
import Modules.operator_scheduler as operator_scheduler
from Audio import audio
import sys

#not compatible jet with The Matrix suite

if __name__ == "__main__":
    args = sys.argv
    
    txt = ["quante volte vuoi dare il cibo ai pesci? ",
       "tra quanto tempo (a partire da ora) vuoi far partire il processo?" +
       " scrivilo in secondi, es. 24 ore = 24*(60**2) ",
       "ogni quanto tempo somministrare il cibo ai pesci? scrivilo in secondi "
       ]
    a = list()
    
    if len(args) != 1:
        if arg.count("--manuale"):
        
            choice = raw_input("stai utilizzando un raspberry, un android o il jack [rpi/android/jack]? ")

                
            for t in txt:
                a.append(raw_input(t))

        elif arg.count("-m") and arg.count("-r") and arg.count("-w") and arg.count("-p"):
            try:
                choice = str(args[args.index("-m") + 1])
                a = [str(args[args.index("-r") + 1]), str(args[args.index("-w") + 1]), str(args[args.index("-p") + 1])]
            except:
                raise
        else:
            exit()#or pass, or continue..
                
        if choice == "rpi":
            module = "from pio import pio" + "\n" + "p = pio()"
            commands = [module, "p.o(True, 11)", "p.o(False, 11, True)"]
        if choice == "jack":
            module = "from audio import AudioFile" + "\n" + "a = AudioFile('sine.wav')"
            commands = [module, "a = AudioFile('sine.wav')\na.playf(2)", "a.close()"]
            
        if choice == "android":
            module = "from paio import android_GPIO"
            commands = [module, "a = android_GPIO()\na.o(state = '1')","a.o(state = '0')"]

        arguments = [int(a[0]),int(a[1]), 5, int(a[2])]
        operator_scheduler.clock(commands, arguments)

    else:
        print ("""
uso: python acquarofilo.py [opzioni elencate sotto]
opzioni:
    --manuale <- il programma chiede all'utente i dati da inserire altrimenti usare tutte le opzioni sottostanti
    -m [rpi/jack/android]
    -r %s
    -w %s
    -p %s""" % (txt[0],txt[1],txt[2]))

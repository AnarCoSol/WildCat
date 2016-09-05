import sys
import os
import time

from Modules.Text_manipulator import Text_manipulator

class Torrent_adder():
    def __init__(self):
        self.tm = Text_manipulator()
        self.torr_links = list()
        self.torr_file = str()

    def Add(self, magnet):
        try:
            stat = os.system("qbittorrent " + magnet)
            if stat == 512:
                print "[-] torrent magnet link" + "\n" + magnet + "\n" + "not added"
                return
        except:
            print "[-] torrent magnet link" + "\n" + magnet + "\n" + "not added" + "\n"
            return
        
        print "[+] torrent magnet link" + "\n" + magnet + "\n" + "added" + "\n"
    def Add_from_file(self, torr_file = str()):
        try:
            raw = self.tm.Read(torr_file).split("\n")
            for magnet in raw:
                self.Add(magnet)
        except:
            raise
if __name__ == "__main__":
    arg = sys.argv
    Ta = Torrent_adder()
    if len(arg) == 1:
        print "usage python torrent_add.py [file.txt/magnet_link/manual]"
    elif len(arg) == 2:
        if arg[1] == "manual":
            while True:
                try:
                    out = "inserisci il magnet link, lascia vuoto o Ctrl+D per uscire: "
                    answer = raw_input(out)
                except KeyboardInterrupt:
                    break
                if answer != str():
                    Ta.Add()
                else:
                    break
        if arg[1][-4:] == ".txt":
            Ta.Add_from_file(arg[1])
        else:
            Ta.Add(arg[1])
                
        
    else:
        print "too arguments passed!"
    exit()

#python sl4a script for android flashlight toggle
#leds are on: /sys/class/leds/flashlight/brightness
#on the fly...WARN
import sys
import os

class android_GPIO():
        def __init__(self):
                self.flashlight = "/sys/class/leds/flashlight/brightness"

        def o(self, pin = str(), state = int()):
                if pin == str():
                        pin = self.flashlight

                if state == "True" or state == "on":
                        state = "1"
                        
                elif state == "False" or state == "off":
                        state = "0"
                        
                print "echo " + str(state) + " > " + pin        
                os.system("echo " + str(state) + " > " + pin)

                
if __name__ == "__main__":
        args = sys.argv
        if len(args) == 1:
                args.append(raw_input("[?] on/off? [1/0][True/False][on/off]"))
        
        a = android_GPIO()
        a.o(state = args[1])

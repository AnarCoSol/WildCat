import sys
import os
import RPi.GPIO as GPIO
class pio():
    def __init__(self):
        self.pin = -1
        self.state = bool()
    def i(self,pin =  -1):
        if pin == -1:
            pin = self.pin
            
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(n, GPIO.IN)
        #GPIO.cleanup()
        
    def o(self,state, pin = -1, clean = False): #state = True v False, pin (numbered counting the pin, red was 11)
        if pin == -1:
            pin = self.pin
            
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, state)
        if clean == True:
            GPIO.cleanup()
#simple usage of pio class
if __name__ == "__main__":
    p = pio()


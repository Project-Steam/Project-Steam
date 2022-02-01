import tm1637
from time import sleep
from time import *
import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings(False)

switch1 = 23
switch2 = 24
switch3 = 16
tm = tm1637.TM1637(21,20, brightness=1)

#GPIO.setup( tm, GPIO.OUT )
GPIO.setup( switch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.setup( switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.setup( switch3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
        
def data():
    while(True):
        #Gamename scroll
        if(GPIO.input( switch1)):
            tm.scroll('Gamenaam')          
            continue
        
        #Datum scroll
        elif(GPIO.input(switch2)):
            tm.scroll('datum')
            continue
        
        #Spelers scroll
        elif(GPIO.input(switch3)):
            tm.scroll('Spelers')
            continue

Spelers = 'shika'

data()
 
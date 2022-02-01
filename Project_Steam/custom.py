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



def start():
    file = open('dates.txt', 'r')
    lines = file.readlines()
    word_list = []

    for i in lines:
        word_list.append(i.split(' '))
        print(word_list)
        global date
        global amount_of_players
        global play_time
        global game_name
        date = i.split(' ')[0].replace('/','-')
        amount_of_players = i.split(' ')[2]
        #play_time = i.split(' ')[4]
        play_time = i.split(' ')[4].replace(':','-')
        game_name = i.split(' ')[6].replace(' ','-')
        print(f'd: {date} p: {amount_of_players} t: {play_time} g: {game_name}')
        i.strip()

        file.close()
        data()

def data():
     while(True):
        #Gamename scroll
        if(GPIO.input( switch1)):
            tm.scroll(game_name)
        
        #Datum scroll
        elif(GPIO.input(switch2)):
            tm.scroll(date)
            tm.scroll(play_time)

        #Spelers scroll
        elif(GPIO.input(switch3)):
            tm.scroll('Amount of players ' + amount_of_players)

start()

print(date)


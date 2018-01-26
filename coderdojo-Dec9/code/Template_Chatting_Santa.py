import os, time
import pygame
import random
import turtle
from turtle import *
from random import randint
import signal
import sys

def santa( text ):
    os.system("espeak ' " + text + " ' ")
    
SOUNDS_PATH='/home/pi/coderdojo-Dec9/sounds/'



santa("Merry Christmas")

time.sleep(0.5)

santa("Hello, what is your name?")
name = input('What is your name: ')
time.sleep(1)
santa("Nice to meet you. " + name)

santa("What gift do you want for Christmas? ")
gift = input("What gift do you want for Christmas: ")
santa( gift + " seems interesting.")
time.sleep(1)

santa(" Do you want to listen to a Christmas song")
time.sleep(1)
song = input("Do you want to listen to a Christmas Song? (yes/no): ")
if song == 'yes':
    santa(" Ok. Let me play a nice song for you ")
    songs = ['FN', 'HJ', 'JBR'] 
    song_name = random.choice(songs)
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load( os.path.join(SOUNDS_PATH, song_name +".mp3") )
    pygame.mixer.music.play(1)
if song == 'no':
    santa("ok")

while pygame.mixer.music.get_busy(): 
          pygame.time.Clock().tick(10)

santa("Good Bye and Merry Christmas")



    

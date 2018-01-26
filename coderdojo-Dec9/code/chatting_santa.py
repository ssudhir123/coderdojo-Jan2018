import os, time
import pygame
import random
import turtle
from turtle import *
from random import randint


import signal
import sys

def signal_handler(signal, frame):
        print ('You pressed Ctrl+C!. Exiting now !!!')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)



    
SOUNDS_PATH='/home/pi/coderdojo-Dec9/sounds/'

pygame.init()


'''
    Let us make a santa that can speak. This is done by createing a
    function that takes the text and speaks it out.
    The text to speak can be anything you want it to talk.

'''

def santa( text ):
    os.system("espeak ' " + text + " ' ")

def play_rock_paper_scissors():


 
    #create a list of play options
    t = ["Rock", "Paper", "Scissors"]
     
    #assign a random play to the computer
    computer = t[randint(0,2)]
     
    #set player to False
    player = False
    counter = 0 
    while player == False:
    #set player to True
        player = input("Rock, Paper, Scissors: ")
        if player == computer:
            print("Tie!")
            counter = counter +1
            if counter == 4:
                    player = True
                    break
            
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                counter = counter +1
                if counter == 4:
                    player = True
                    break
                
            else:
                print("You win!", player, "smashes", computer)
                counter = counter +1
                if counter == 4:
                    player = True
                    break
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                counter = counter +1
                if counter == 4:
                    player = True
                    break
            else:
                print("You win!", player, "covers", computer)
                counter = counter +1
                if counter == 4:
                    player = True
                    break
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                counter = counter +1
                if counter == 4:
                    player = True
                    break
            else:
                print("You win!", player, "cut", computer)
                counter = counter +1
                if counter == 4:
                    player = True
                    break
        else:
            print("That's not a valid play. Check your spelling!")
        #player was set to True, but we want it to be False so the loop continues
        player = False

def draw_tree():

    screen = turtle.Screen()
    screen.setup(800,600)

    circle = turtle.Turtle()
    circle.shape('circle')
    circle.color('red')
    circle.speed('fastest')
    circle.up()

    square = turtle.Turtle()
    square.shape('square')
    square.color('green')
    square.speed('fastest')
    square.up()

    circle.goto(0,280)
    circle.stamp()

    k = 0
    for i in range(1, 17):
        y = 30*i
        for j in range(i-k):
            x = 30*j
            square.goto(x,-y+280)
            square.stamp()
            square.goto(-x,-y+280)
            square.stamp()

        if i % 4 == 0:
            x =  30*(j+1)
            circle.color('red')
            circle.goto(-x,-y+280)
            circle.stamp()
            circle.goto(x,-y+280)
            circle.stamp()        
            k += 2

        if i % 4 == 3:
            x =  30*(j+1)
            circle.color('yellow')
            circle.goto(-x,-y+280)
            circle.stamp()
            circle.goto(x,-y+280)
            circle.stamp() 

    square.color('brown')
    for i in range(17,20):
        y = 30*i
        for j in range(3):    
            x = 30*j
            square.goto(x,-y+280)
            square.stamp()
            square.goto(-x,-y+280)
            square.stamp()   


def draw_another_tree( size):

        n = size*1.


        speed("fastest")
        left(90)
        forward(3*n)
        color("orange", "yellow")
        begin_fill()
        left(126)
        for i in range(5):
            forward(n/5)
            right(144)
            forward(n/5)
            left(72)
        end_fill()
        right(126)

        color("dark green")
        backward(n*4.8)
        def tree(d, s):
            if d <= 0: return
            forward(s)
            tree(d-1, s*.8)
            right(120)
            tree(d-3, s*.5)
            right(120)
            tree(d-3, s*.5)
            right(120)
            backward(s)
        tree(15, n)
        backward(n/2)


def second_tree():
        import sys
        w = sys.stdout.write
        def t(n,s):
            for i in range(n):
                for a in range(n-i):
                    w(" ")
                w("[")
                for l in range(i<<1):
                    if i==n-1:
                        w("_")
                    else:
                        w("~")
                w("]")
                print("")
            for o in range(s):
                for i in range(n):
                    w(" ")
                print("[]")

        t(10, 2)

def talk_to_santa():

    '''
     Say a greet message and then sing the Santa song.
    '''
    santa("Merry Christmas")


    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
    pygame.init()
    pygame.mixer.init()
    sounds = ['greeting-bells', 'greetings',]
    for sound_name in sounds:
            pygame.mixer.music.load( os.path.join(SOUNDS_PATH, sound_name +".mp3") )
            pygame.mixer.music.play(1)
            while pygame.mixer.music.get_busy(): 
                    pygame.time.Clock().tick(10)
    time.sleep(0.5) 
    santa("Hello, what is your name?")
    name = input('What is your name: ')
    time.sleep(1)
    santa("Nice to meet you. " + name)


    time.sleep(1)
    santa("Do you want to draw a christmas tree ? ")
    answer = input("Do you want to draw a christmas tree? (yes/no):" )
    if answer == 'yes':
            draw_tree()
            turtle.exitonclick()
            time.sleep(1)
            santa("Nice Job " + name )
    else:
        santa("OK. Lets move to something else")
        
            

    
    
    time.sleep(0.5)
    
    santa("Do you want to draw another christmas tree?") 
    answer = input("Do you want to draw another christmas tree? (yes/no): " )
    
    if answer == 'yes':
            second_tree()
    else:
            santa("ok. Lets do something else.")
        
    santa("What gift do you want for Christmas? ")
    gift = input("What gift do you want for Christmas: ")
    santa( gift + " seems interesting.")
    time.sleep(1) 
   
    santa("Do you want to hear a joke?")
    answer = input("Do you want to hear a joke (yes/no): ") 
    if answer == ('yes'):
        santa("Whos my favorite musician?")
        time.sleep(0.5) 
        print("ELF-is Presley!") 
        santa("Elf-is Presley!")
        time.sleep(0.4)
        santa("Get it?")
    if answer == ('no'):
        santa("Ok then, sometimes its better to be silent.")
    time.sleep(1) 
    
    santa("Do you want to play rock paper scissors with me ? ")
    response = input("Do you want to play rock paper scissors with me(yes/no): ")
    if response == 'yes':
            play_rock_paper_scissors()
    else:
            santa("Lets do something else then") 
    time.sleep(1)
    
    santa(" Do you want to listen to a Christmas song")
    time.sleep(1)
    song = input("Do you want to listen to a Christmas Song? (yes/no): ")
    if song == 'yes':
            santa(" Ok. Let me play a nice song for you ")
            songs = ['FN', 'HJ', 'JBR'] 
            song_name = random.choice(songs) 
            pygame.mixer.music.load( os.path.join(SOUNDS_PATH, song_name +".mp3") )
            pygame.mixer.music.play(1)
    if song == 'no':
            santa("ok")

    while pygame.mixer.music.get_busy(): 
          pygame.time.Clock().tick(10)

    santa("Good Bye and Merry Christmas")

    sys.exit(0)
    

    
    time.sleep(1)

    
if __name__ == '__main__':
    talk_to_santa()
        

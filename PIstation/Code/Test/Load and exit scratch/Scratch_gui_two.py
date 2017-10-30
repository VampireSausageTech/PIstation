import os
import subprocess
from Tkinter import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
programopen=False
window = Tk()
window.title("PIstation game launcher")
directory = "/home/pi/PIstation/Games/Scratch"
result = os.listdir(directory)
listlen = len(result)
num = 0
window.attributes("-fullscreen",True)
gametext = ""
programopen = False
gameprocess = ""
def menu():
        text = open("/home/pi/PIstation/Code/Files/Command.txt", "w")
        text.write("Menu")
        text.close()
        exit()
def exit_fullscreen (event) :
        window.attributes("-fullscreen",False)
def load():
        global programopen
        global gameprocess
        minidirectory = "/home/pi/PIstation/Games/Scratch"
        game = entry.get()
        directory = "/home/pi/PIstation/Games/Scratch"
        result = os.listdir("/home/pi/PIstation/Games/Scratch")
        print game
        print result
        if game in result:
                gamedir = minidirectory + "/" + game
                gamecommand = ["scratch", "presentation", gamedir]
                print gamecommand
                print gametext
                gameprocess = subprocess.Popen(gamecommand)
                programopen = True

def check():
        global gameprocess
        global programopen
        if GPIO.input(3)and programopen == True:
            gameprocess.terminate()
            print("Game Exited")
            programopen = False
        window.after(100, check)
        


while num < listlen:
    Label(window, text=result[num]).grid(row=num, column=0, sticky=W)
    num = num + 1

Label(window, text="\nType in the game you want to load in the text box then press Load.").grid(row=num, column=0, sticky=W)
num = num + 1
entry = Entry(window, width=20, text="Type in the game you want to launch here.")
entry.grid(row=num, column=0, columnspan=3, sticky=W)
num = num + 1
Button(window, text="Load", width=5, command=load).grid(row=num, column=0, sticky=W)
num = num + 1
Button(window, text="Exit", width=5, command=menu).grid(row=num, column=0, sticky=W)
#Launch as sudo
window.bind("<Escape>", exit_fullscreen)
window.after(100, check)
window.mainloop()

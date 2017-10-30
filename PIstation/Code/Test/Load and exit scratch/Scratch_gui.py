import os
from Tkinter import *
window = Tk()
window.title("PIstation game launcher")
directory = "/home/pi/PIstation/Games/Scratch"
result = os.listdir(directory)
listlen = len(result)
num = 0
window.attributes("-fullscreen",True)
def menu():
        text = open("/home/pi/PIstation/Code/Files/Command.txt", "w")
        text.write("Menu")
        text.close()
def exit_fullscreen (event) :
        window.attributes("-fullscreen",False)
def load():
    minidirectory = "/home/pi/PIstation/Games/Scratch"
    game = entry.get()
    print game
    if game in result:
        minidirectory= minidirectory + "/" + game
        text = open("/home/pi/PIstation/Code/Files/dir.txt", "w")
        text.write(minidirectory)
        run = open("/home/pi/PIstation/Code/Files/run.txt", "w")
        run.write("yes")



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
window.mainloop()

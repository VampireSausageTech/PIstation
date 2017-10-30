import os, time, subprocess
from Tkinter import *
window = Tk()
window.title("PIstation game launcher")
# canvas width = (width/3)*2 button width = width / 3
window.attributes("-fullscreen",True)
def exit_program():
    text = open("/home/pi/PIstation/Code/Files/Command.txt", "w")
    text.write("Exit")
    text.close()
def exit_fullscreen (event) :
        window.attributes("-fullscreen",False)
def code():
    text = open("/home/pi/PIstation/Code/Files/Command.txt", "w")
    text.write("Code")
    text.close()
def Load():
    text = open("/home/pi/PIstation/Code/Files/Command.txt", "w")
    text.write("Load")
    text.close()

hight = window.winfo_screenheight()
width =  window.winfo_screenwidth()
print hight

cwidth = width / 3
print cwidth
bwidth = 640
bh = 360
cwidth = cwidth * 2
imglist = ["/home/pi/PIstation/Code/Files/Logo_Menu.gif",
"/home/pi/PIstation/Code/Files/python.gif"]
imgnum = 0
print cwidth


ButtonImage = PhotoImage(file='/home/pi/PIstation/Code/Files/Logo_Menu.gif')
Label = Label(window, image=ButtonImage, height=hight, width=cwidth, bg="white").grid(row=0, column=0, columnspan=4, rowspan=4, sticky=W)

Play = PhotoImage(file='/home/pi/PIstation/Code/Files/Play.gif')
Code = PhotoImage(file='/home/pi/PIstation/Code/Files/Code.gif')
Exit = PhotoImage(file='/home/pi/PIstation/Code/Files/Exit.gif')

Button(window, image=Play, height=bh, width=bwidth, command=Load, highlightthickness=1).grid(row=0, column=4, columnspan=4, sticky=N)
Button(window, image=Code, height=bh, width=bwidth, command=code, bg="white", highlightthickness=1).grid(row=1, column=4, columnspan=4, sticky=N)
Button(window, image=Exit, height=bh, width=bwidth, command=exit_program, highlightthickness=1).grid(row=2, column=4, columnspan=4, sticky=N)
window.bind("<Escape>", exit_fullscreen)
window.mainloop()

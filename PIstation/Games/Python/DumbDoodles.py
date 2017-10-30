#! /usr/bin/env python

from Tkinter import *

window = Tk()
window.title("Dumb_Doodles_PC")
canvas_height = window.winfo_screenheight()
canvas_width = window.winfo_screenwidth()
window.attributes("-fullscreen",True)

canvas_colour = "black"
p1_x = canvas_width/2
p1_y = canvas_height/2
p1_colour = "blue"
line_width = 5
line_length = 5

def p1_move_N (event) :
	global p1_y
	canvas.create_line(p1_x, p1_y, p1_x, (p1_y-line_length), width=line_width, fill=p1_colour)
	p1_y = p1_y - line_length

def p1_move_S (event) :
	global p1_y
	canvas.create_line(p1_x, p1_y, p1_x, p1_y+line_length, width=line_width, fill=p1_colour)
	p1_y = p1_y + line_length
 
def p1_move_E (event) :
	global p1_x
	canvas.create_line(p1_x, p1_y, p1_x + line_length, p1_y, width=line_width, fill=p1_colour)
	p1_x = p1_x + line_length

def p1_move_W (event) :
	global p1_x
	canvas.create_line(p1_x, p1_y, p1_x - line_length, p1_y, width=line_width, fill=p1_colour)
	p1_x = p1_x - line_length
def erase (event) :
        canvas.delete("all")
def exit_fullscreen (event) :
        window.attributes("-fullscreen",False)
def move (event) :
        global p1_x
        global p1_y
        p1_x, p1_y = event.x, event.y
def colour (event) :
        global p1_colour
        if p1_colour == "blue" :
                p1_colour = "green"
        else:
                p1_colour = "blue"
window.bind("<Escape>", exit_fullscreen)
window.bind("<Up>", p1_move_N)
window.bind("<Down>", p1_move_S)
window.bind("<Left>", p1_move_W)
window.bind("<Right>", p1_move_E)
window.bind("<space>", erase)
window.bind("<Button-1>", move)
window.bind("<Button-3>", colour)
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

window.mainloop()

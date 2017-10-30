import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
programopen=False
def open_game():
    with open("/home/pi/PIstation/Code/Files/dir.txt", "r") as game:
        gametext = game.read()
        minidirectory = "/home/pi/PIstation/Games/Scratch"
        gametext = str(minidirectory) + "/" + str(game)
        gamedir = gametext
        gamecommand = ["scratch", "presentation", gamedir]
        print gamecommand
        print gametext
        gameprocess = subprocess.Popen(gamecommand)
        run = open("/home/pi/PIstation/Code/Files/run.txt", "w")
        run.write("")
        programopen = True

    def close_game():
        gameprocess.terminate()

with open("/home/pi/PIstation/Code/Files/run.txt", "r") as run:
    runtext = run.read()
    if runtext == "yes":
        open_game()
        
if GPIO.input(3)and programopen == True:
    close_game()
    print("Game Exited")
    programopen = False

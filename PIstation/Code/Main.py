import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
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
text = open("/home/pi/PIstation/Code/Files/Command.txt", "w")
text.write("")
text.close()
textfile = open("/home/pi/PIstation/Code/Files/Command.txt", "r")
game = open("/home/pi/PIstation/Code/Files/dir.txt", "r")
args = ["sudo", "python", "/home/pi/PIstation/Code/Main Menu/Main_test_two.py"]
run = open("/home/pi/PIstation/Code/Files/run.txt", "r")
process = subprocess.Popen(args)
print("hello")
Program = "Menu"
programopen = False
open_menu = False
continue_running = True
def kill_scratch():
    gameprocess.terminate()
while continue_running == True:
    with open("/home/pi/PIstation/Code/Files/Command.txt", "r") as textfile:
        text = textfile.read()
        if text == "Exit":
            process.terminate()
            if programopen == True:
                gameprocess.terminate()
            continue_running = False
        if text == "Load" and Program != "Load":
            process.terminate()
            args = ["sudo", "python", "/home/pi/PIstation/Code/Load and exit scratch/Scratch_gui.py"]
            process = subprocess.Popen(args)
            Program = "Load"

        if text == "Code" and Program != "Code":
            print("Scratch")
            process.terminate()
            args = ["scratch"]
            process = subprocess.Popen(args)
            Program = "Code"
            var = raw_input("Press enter when you are ready to return to the menu.\n")
            process.terminate()
            args = ["sudo", "python", "/home/pi/PIstation/Code/Main Menu/Main_test_two.py"]
            process = subprocess.Popen(args)
            Program = "Menu"
            open_menu = False
            textfile_two = open("/home/pi/PIstation/Code/Files/Command.txt", "w")
            textfile_two.write("Menu")
            text = textfile.read()
            
        if text == "Menu" and Program != "Menu":
            process.terminate()
            args = ["sudo", "python", "/home/pi/PIstation/Code/Main Menu/Main_test_two.py"]
            process = subprocess.Popen(args)
            Program = "Menu"
            open_menu = False

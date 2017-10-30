import os
import subprocess
directory = "/home/pi/PIstation/Games/Scratch"
result = os.listdir(directory)
print("\n")
listlen = len(result)
num = 0
while num < listlen:
    print result[num]
    num = num + 1
game = raw_input("What game do you want to play?\n")
directory = directory + "/" + game
print directory
#Launch as sudo

args = ["scratch", "presentation", directory]
process = subprocess.Popen(args)
raw_input("Press enter to exit ")
process.terminate()

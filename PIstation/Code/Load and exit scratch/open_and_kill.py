#Launch as sudo
import subprocess
scratch_script = "/home/pi/test.sb"
args = ["scratch", "presentation", scratch_script]
process = subprocess.Popen(args)
raw_input("Press enter to exit ")
process.terminate()

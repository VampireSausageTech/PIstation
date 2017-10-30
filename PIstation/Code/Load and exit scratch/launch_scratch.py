import sys
import subprocess


def open_scratch_presentation(scratch_script):
    args = ["scratch", "presentation", scratch_script]
    print "Launching Scratch program: %s" % scratch_script
    process = subprocess.Popen(args)

    print "Scratch program launched with PID (%s)" % process.pid

    return process


def main(script):
    open_scratch_presentation(script)


if __name__ == '__main__':
    main(sys.argv[1])

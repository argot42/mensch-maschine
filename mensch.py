#!/usr/bin/python

from sys import stdout, argv
from time import sleep
import getopt

class fm:
    p = '\033[95m' # purple
    c = '\033[96m' # cyan
    dc = '\033[36m' # darkcyan
    b = '\033[94m' # blue
    g = '\033[92m' # green
    y = '\003[93m' # yellow
    r = '\033[91m' # red
    b = '\033[1m' # bold
    un = '\033[4m' # underline
    end = '\033[0m' # end

def usage():
    print("""{0}Usage{1}
  {3} [OPTIONAL FLAGS]

{0}Options:{1}
{2}-w, --word{1}          Printed word.
{2}-f, --first{1}         First delay.
{2}-l, --last{1}          Letter coloring delay.\
""".format(fm.un, fm.end, fm.b, argv[0]))

MAN = "MACHINE"
LINES = len(MAN)
FIRST_DELAY = .5
LAST_DELAY = .25
COLOR = fm.r

try:
    opts, args = getopt.getopt(argv[1:], "hw:f:l:", ["help", "word=", "first=", "last="])


    for option, argument in opts:
        if option in ("-h", "--help"):
            usage()
            exit()

        elif option in ("-w", "--word"):
            MAN = str(argument)
            LINES = len(MAN)

        elif option in ("-f", "--first"):
            FIRST_DELAY = float(argument) 

        elif option in ("-l", "--last"):
            LAST_DELAY = float(argument)

        else:
            assert False, "unhandled option"

except getopt.GetoptError as err:
    usage()
    print(err)
    exit(2)



# THE MAN
# MACHINE, MACHINE, MACHINE ...

stdout.write("\n" * LINES)

for i in range(LINES - 1, -1, -1):
    stdout.write('\b' * len(MAN) * 2)
    stdout.write('\r' + ' ' * (LINES - i - 1) + MAN)
    stdout.flush()
    
    sleep(FIRST_DELAY)

#sleep(MID_DELAY)

# MACHIIIINEE

for i in range(LINES):
    colorified = MAN[:i] + fm.b + COLOR + MAN[i] + fm.end + MAN[(i+1):]
    stdout.write('\r' + ' ' * (LINES - i - 1) + colorified + '\n')
    stdout.flush()

    sleep(LAST_DELAY)

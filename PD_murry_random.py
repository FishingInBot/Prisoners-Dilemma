import sys
import random

def choice():
    if (random.randint(0,1) == 1):
        return 'C'
    else:
        return 'D'

def PD_murry_random(myHist, oppHist):
    return choice()

if __name__ == "__main__":
    sys.stderr.write("ERROR - this is not intended to be run stand-alone\n")
    exit(-1)
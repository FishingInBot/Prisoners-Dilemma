import sys
import random

def PD_murry_random70(myHist, oppHist, myScore, oppScore):
    if (random.randint(1,100) <= 70):
        return 'C'
    else:
        return 'D'

if __name__ == "__main__":
    sys.stderr.write("ERROR - this is not intended to be run stand-alone\n")
    exit(-1)
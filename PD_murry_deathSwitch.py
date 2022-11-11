import sys

def PD_murry_deathSwitch(myHist, oppHist, myScore, oppScore):
    if ('D' in oppHist):
        return 'D'
    elif (myScore < oppScore):
        return 'D'
    else:
        return 'C'

if __name__ == "__main__":
    sys.stderr.write("ERROR - this is not intended to be run stand-alone\n")
    exit(-1)
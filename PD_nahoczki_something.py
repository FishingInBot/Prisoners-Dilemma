import sys
import random


def choice(history, oppHistory):
    if not history:
        return 'D'
    elif history[-1] == 'D' and oppHistory[-1] == 'D':
        return 'D'
    else:
        return oppHistory[-1]


def PD_nahoczki_something(myHist, oppHist):
    return choice(myHist, oppHist)


if __name__ == "__main__":
    sys.stderr.write("ERROR - this is not intended to be run stand-alone\n")
    exit(-1)

import sys

def PD_murry_WSLS(myHist, oppHist, myScore, oppScore):
    if oppHist == []:
        return 'C'
    elif ('D' == oppHist[-1]):
        if ('C' == myHist[-1]):
            return 'D'
        else:
            return 'C'
    else:
        return myHist[-1]

if __name__ == "__main__":
    sys.stderr.write("ERROR - this is not intended to be run stand-alone\n")
    exit(-1)
import sys

def PD_murry_greedy(myHist, oppHist, myScore, oppScore):
    startingCode = ['C', 'D', 'D', 'C', 'C']
    oppStartCode = ['C', 'D', 'D', 'C', 'C']
    if ((myScore - oppScore) >= 50):
        return 'D'
    elif len(oppHist) < len(startingCode):
        return startingCode[len(oppHist)]
    elif (oppHist[:len(startingCode)] == oppStartCode) or ('D' not in oppHist):
        return 'D'
    else:
        if(myHist[-1] == oppHist[-1] == 'D') and oppHist[-2] != 'C':
            return 'C'
        return oppHist[-1]

if __name__ == "__main__":
    sys.stderr.write("ERROR - this is not intended to be run stand-alone\n")
    exit(-1)
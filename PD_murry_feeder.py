import sys

def PD_murry_feeder(myHist, oppHist, myScore, oppScore):
    startingCode = ['C', 'D', 'D', 'C', 'C']
    oppStartCode = ['C', 'D', 'D', 'C', 'C']
    if len(oppHist) < len(startingCode):
        return startingCode[len(oppHist)]
    elif (oppHist[:len(startingCode)] == oppStartCode):
        return 'C'
    elif ((oppScore - myScore)>50):
        return 'C'
    else:
        return 'D'
        

if __name__ == "__main__":
    sys.stderr.write("ERROR - this is not intended to be run stand-alone\n")
    exit(-1)
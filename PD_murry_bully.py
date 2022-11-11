import sys

def PD_murry_bully(myHist, oppHist, myScore, oppScore):
    if oppHist == []:
        return 'C'
    elif oppHist[-1] == 'C':
        return 'D'
    else:
        return 'C'

if __name__ == "__main__":
    sys.stderr.write("ERROR - this is not intended to be run stand-alone\n")
    exit(-1)
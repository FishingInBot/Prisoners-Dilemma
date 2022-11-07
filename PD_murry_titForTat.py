import sys

def choice(past):
    if past == []:
        return 'C'
    else:
        return past[-1]

def PD_murry_titForTat(myHist, oppHist):
    return choice(oppHist)

if __name__ == "__main__":
    sys.stderr.write("ERROR - this is not intended to be run stand-alone\n")
    exit(-1)

""" 
This is my attempt to read all python files in a the folder this runs in and use them to compete with eachother round robin style
in the prisoner's dillema problem.

Outline game with numbers, Standard PD with unknown end. I want about 200 min runs with an average of 250 and max 300.
IE: 200+(1..100) rounded down.
Game will be scored with the following table:
C = cooperate, D = Defect

    C    D
C  3,3 | 5,0
   ----+----    
D  0,5 | 1,1

AKA mutual cooperation will net 3 points each, defection against cooperation will give the defector 5 points and 
the cooperator nothing, while double defect will net a single point each.

The fun of this game is acknowledging the seeming paradox that GTO play on a single iteration of this game is to
always defect. This is because no matter what your opponent does, you get more points defecting that cooperating.
This shifts when we want to maximize points over many attempts as a mutual agreement will gain more than mutual 
defection (gaining 3 points/round vs 1). 

Things to do: TODO
   Track matchups and ensure we are playing round robin correctly,
   Output matches and point values to text files to verify,
   Determine winning strategy and make changes from there,
   Put in some standard strategies to make mock data,

   
    Ideas: How to store score for unknown number of files at launch?
                Make a map and loop in keys with the name of files, update map values with score after each game...?

"""

import importlib
import random
import os
import pathlib


numGames = 2
minRounds = 100
maxRounds = 300




def p1Choice(past):
    if (random.randint(0,1) == 1):
        return 'C'
    else:
        return 'D'


def p2Choice(past):
    if past == []:
        return 'C'
    else:
        return past[-1]

def findContestants():
    entries = os.listdir(path = "C:/Users/14143/Documents/PD ThIng")
    for entry in entries:
        if entry == f"PD_*":
            print(entry)

def get_algos(path = pathlib.Path(__file__).parent.resolve()):
    flist = sorted(os.listdir(path))
    algoList = []
    for fname in flist:
        if (fname.startswith("PD_")) and fname[-len(".py") == ".py"]:
            algoList.append(fname[:-len(".py")])
    algoFunc = []
    algoScores = []
    for algo in algoList:
        algoFunc.append(getattr(importlib.import_module(algo), algo))
        algoScores.append([])
    return algoList, algoFunc, algoScores

#currently set to run {numGames} games.
def playGame(p1Fun, p2Fun):
    # This will keep track of game wins, though only useful in determining 1-on-1 fights.
    p1Games = 0
    p2Games = 0
    p1Score = []
    p2Score = []
    for int in range(1,numGames+1):
        # Here we are keeping score for the two players, the grids will store their selections on each pass.
        player1Score = 0
        player2Score = 0

        # rounds = total rounds on each pass, currentRound is current round 
        rounds = random.randint(minRounds,maxRounds)
        currentRound = 0

        #player choice history
        playerOneGrid = []
        playerTwoGrid = []

        # Lets us know how many passes are going, but never tells the players.
        print(f"{rounds} runs going....") 

        """
        Here we are taking imput from the contestants.
        Need to convert this to file calls for other .py files in folder.
        """
        while currentRound < rounds:

            #Call competing functions given up to the last 5 choices from each player. This is all the data they can use for their functions.
            if currentRound>= 5:
                player1Choice = p1Fun(playerOneGrid[-5:],playerTwoGrid[-5:])
                player2Choice = p2Fun(playerTwoGrid[-5:],playerOneGrid[-5:])
            else:
                player1Choice = p1Fun(playerOneGrid[-currentRound:],playerTwoGrid[-currentRound:])
                player2Choice = p2Fun(playerTwoGrid[-currentRound:],playerOneGrid[-currentRound:])

            # If someone gives me bad inputs I will have to filter to C by default because that is most benificial to opponent. So if not 'D', will be 'C' by force...
            if player1Choice != 'D':
                player1Choice = 'C'
            if player2Choice != 'D':
                player2Choice = 'C'

            # Scoring updates
            if player1Choice == 'C' and player2Choice == 'C':
                player1Score += 3
                player2Score += 3
            elif player1Choice == 'D' and player2Choice == 'C':
                player1Score += 5
            elif player1Choice == 'C' and player2Choice == 'D':
                player2Score += 5
            else:
                player1Score += 1
                player2Score += 1

            # Deduct currentRound and update grids.
            currentRound += 1
            playerOneGrid.append(player1Choice)
            playerTwoGrid.append(player2Choice)

        if player1Score > player2Score:
            p1Games += 1
        elif player2Score > player1Score:
            p2Games += 1

        p1Score.append(player1Score/rounds)
        p2Score.append(player2Score/rounds)

        print(f"At the end: \n{player1Score/rounds}/round is player 1's score,\n{player2Score/rounds}/round is player 2's score.\nChoices were as follows:\n")
        print(playerOneGrid)
        print (playerTwoGrid)

    print(f"{p1Games} for player 1, {p2Games} for player 2. {numGames-(p2Games+p1Games)} were a draw.")
    return p1Score, p2Score

def main():
    algolist, algoFunc, algoScores = get_algos()
    print(f"algolist = {algolist}, algoFunc =  {algoFunc}")
    for index1 in range(len(algolist)):
        for index2 in range(index1+1,len(algolist)):
            p1Score, p2Score = playGame(algoFunc[index1], algoFunc[index2])
            for score in p1Score:
                algoScores[index1].append(score)
            for score in p2Score:
                algoScores[index2].append(score)
    finalScore = []
    for list in algoScores:
        sum = 0
        for score in list:
            sum += score
        finalScore.append(sum/len(list))
    print(f"{max(finalScore)} from {algolist[finalScore.index(max(finalScore))]}")

# Standard funny thing...
if __name__ == "__main__":
    main()
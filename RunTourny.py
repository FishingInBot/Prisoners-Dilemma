""" 
Things to do: TODO
   Output matches and point values to text files to verify,
   Update documentation to make it clear what each 'player' needs.
"""

import importlib
import random
import os
import pathlib

#adjustable "constants"
numGames = 1
minRounds = 250
maxRounds = 350
historyLimit = 20
ccPoints = 3
dcPoints = 5

def get_algos(path = pathlib.Path(__file__).parent.resolve()):
    flist = sorted(os.listdir(path))
    algoList = []
    for fname in flist:
        if (fname.startswith("PD_")) and fname.endswith(".py"):
            algoList.append(fname[:-len(".py")])
    algoFunc = []
    algoScores = []
    for algo in algoList:
        print(algo)
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

            #Call competing functions given up to the last {historyLimit} choices from each player. This is all the data they can use for their functions.
            if currentRound>= historyLimit:
                player1Choice = p1Fun(playerOneGrid[-historyLimit:],playerTwoGrid[-historyLimit:], player1Score, player2Score)
                player2Choice = p2Fun(playerTwoGrid[-historyLimit:],playerOneGrid[-historyLimit:], player2Score, player1Score)
            else:
                player1Choice = p1Fun(playerOneGrid[-currentRound:],playerTwoGrid[-currentRound:], player1Score, player2Score)
                player2Choice = p2Fun(playerTwoGrid[-currentRound:],playerOneGrid[-currentRound:], player2Score, player1Score)

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
            print(f"Above was a game from {algolist[index1]} and {algolist[index2]}")
    finalScore = []
    for list in algoScores:
        sum = 0
        for score in list:
            sum += score
        finalScore.append(sum/len(list))
    print(algolist, " ", finalScore)
    while (algolist != []):
        if len(algolist) == 1:
            print(f"{finalScore.pop(0)} from {algolist.pop(0)}")
        else:
            print(f"{finalScore.pop(finalScore.index(max(finalScore)))} from {algolist.pop(finalScore.index(max(finalScore)))}")

# Standard funny thing...
if __name__ == "__main__":
    main()
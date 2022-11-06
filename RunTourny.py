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
   Make a quick and dirty copy that plays against input.
   Track points for each entry (aka file in folder),
   Track matchups and ensure we are playing round robin correctly,
   Compare selections angd give points,
   return previous selections from opponent to both competitors (so they can adapt their strategy)
   Output matches and point values to text files to verify,
   Determine winning strategy and make changes from there,
   Put in some standard strategies to make mock data,

   
    Ideas: How to store score for unknown number of files at launch?
                Make a map and loop in keys with the name of files, update map values with score after each game...?

"""

import random
import os

#This will keep track of game wins, though only useful in determining 1-on-1 fights.
p1Games = 0
p2Games = 0

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
    entries = os.scandir(path = "C:/Users/14143/Documents/PD ThIng")


#currently set to run 50 games.
def main():
    for int in range(1,50):

        """
        Here we are keeping score for the two players, the grids will store their selections on each pass.
        """
        player1Score = 0
        player2Score = 0

        #roundMax = total rounds on each pass, currentRound is current round 
        roundMax = random.randint(200,300)
        currentRound = 0

        playerOneGrid = []
        playerTwoGrid = []

        #lets us know how many passes are going, but never tells the players.
        print(f"{roundMax} runs going....") 

        """
        Here we are taking imput from the contestants.
        Need to convert this to file calls for other .py files in folder.
        """
        while currentRound < roundMax:

            if currentRound>= 5:
                player1Choice = p1Choice(playerTwoGrid[-5:])
                player2Choice = p2Choice(playerOneGrid[-5:])
            else:
                player1Choice = p1Choice(playerTwoGrid[-currentRound:])
                player2Choice = p2Choice(playerOneGrid[-currentRound:])

            #If someone gives me bad inputs I will have to filter to C by default because that is most benificial to opponent. So if not 'D', will be 'C' by force...
            if player1Choice != 'D':
                player1Choice = 'C'
            if player2Choice != 'D':
                player2Choice = 'C'

            #Scoring updates
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

            #deduct currentRound and update grids.
            currentRound += 1
            playerOneGrid.append(player1Choice)
            playerTwoGrid.append(player2Choice)


        print(f"At the end: \n{player1Score} is player 1's score,\n{player2Score} is player 2's score.\nChoices were as follows:\n")
        print(playerOneGrid)
        print (playerTwoGrid)
        if player1Score > player2Score:
            p1Games += 1
        elif player2Score > player1Score:
            p2Games += 1
        
        #print() #TODO get this implemented for pass when you update file calls.

    print(f"{p1Games} for player 1, {p2Games} for player 2. {100-(p2Games+p1Games)} were a draw.")

#standard funny thing...
if __name__ == "__main__":
    main()


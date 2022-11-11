# PD-ThIng
This is my attempt to read all python files in a the folder this runs in and use them to compete with eachother round 
robin style in the prisoner's dillema problem.

Outline game with numbers, Standard PD with unknown runs. I want about 250 min runs with an average of 300 and max 350.
Game will be scored with the following table:
C = cooperate, D = Defect

|     |  C  |  D  |
|:---:|:---:|:---:|  
|  C  | 3,3 | 5,0 |   
|  D  | 0,5 | 1,1 |

AKA mutual cooperation will net 3 points each, defection against cooperation will give the defector 5 points and 
the cooperator nothing, while double defect will net a single point each.

After each game, your total score will be divised by the rounds played to determine an average per round. These will 
then be averaged again to determine how you did vs the average opponent.

The fun of this game is acknowledging the seeming paradox that GTO play on a single iteration of this game is to
always defect. This is because no matter what your opponent does, you get more points defecting that cooperating.
This shifts when we want to maximize points over many attempts as a mutual agreement will gain more than mutual 
defection (gaining 3 points/round vs 1).

USAGE NOTES:
for a submitted file to be eligible, it simply needs to match the naming sceme "PD_lastName_strategyName.py"
and contain a definition for a function with the same name as the file (ie: "def PD_lastName_strategyName:")
followed by your strategy. See PD_murry files for examples on formatting and definitions. After submitting your 
strategy, it will be public and people may possibly extract a strategy to beat yours so be weary.

The parameters for this call will be 2 lists, and 2 ints. in order: your history, opponent history, your score, opponent score.
The history will only show up to 20 of the recent choices from each side.
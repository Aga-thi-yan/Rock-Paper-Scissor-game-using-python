import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK= 1
    PAPER= 2
    SCISSOR= 3

def RPS_GAME():
    while playagain:

        print(RPS.ROCK)
        print(RPS.PAPER)
        print(RPS.SCISSOR)

        print("")
        playerchoice= input("Enter.... \n1 rock,\n2 paper,\n3 scissor:\n\n")
        player= int(playerchoice)

        if player <1 or player >3:
            print("You should enter number between 1, 2, 3.")
            return RPS_GAME
        computer_choice= random.choice("123")

        computer= int(computer_choice)

        print("")
        print("you chose " + str(RPS(player)).replace('RPS.', ''
        )+".")
        print("computer choose " + str(RPS(computer)).replace("RPS.", "" ) + ".")
        print("")

        if player == 1 and computer ==1:
            print(" 🙌Draw")
        elif player == 2 and computer ==2:
            print(" 🙌Draw")
        elif player == 3 and computer ==3:
            print(" 🙌Draw")
        elif player == 1 and computer == 2:
            print("computer wins🤖")
        elif player == 3 and computer == 1:
            print("computer Wins🤖")
        elif player == 2 and computer == 1:
            print("computer Wins🤖")
        else:
            print( "Player wins👍")

        playagain = input("\n play again ? \nEnter y for yes\n Enter n for no \n \n" )

        if playagain.lower() == "y":
            return RPS_GAME
        
        else:
            print("Thank You for Playing .🙌🍾🎉")
            playagain = False

            sys.exit("Bye!👋")
            
RPS_GAME()          

        
#RPS.py
#Name:Emily Billings
#Date: 9-12-25
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

playAgain = "Y"
while playAgain == "Y": 

  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish. 
computer = random.choice( ["R", "P", "S"] )
player = input("Pick your weapon (R, P, S): ")
  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection

  #Determine winner and state what happened to the user
if computer == "R":
  print("computer chose Rock")
elif computer == "P":
  print("Computer chose Paper")
else:
 print("Computer chose Scissors")


 if player == "R":
  print("Player chose Rock")
 elif player == "P":
  print("Player chose Paper")
 else:
  print("Player chose Scissors")

  if player == "R" and computer =="R":
   print("Tie")
   ties = ties + 1
   if player == "R" and computer == "P":
    print("Computer wins.")
   losses = losses + 1
   if player == "R" and computer =="S":
    print("You win!")
    wins = wins + 1 

playAgain = input("Play again (Y/N): ")
  #In the end, print the stats
 print("Wins \t Ties \t Losses")
 print("---- \t ---- \t ------")
 print(Wins, "\t", ties , "\t", losses) 

 if __name__ == '__main__':
 main()

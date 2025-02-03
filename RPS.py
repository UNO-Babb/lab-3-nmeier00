#RPS.py
#Name: Nick Meier 
#Date: February 3 2025
#Assignment: Lab 3
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  playAgain= "Y"
  while playAgain== "Y":

    #Randomly choose the computer between 'R', 'P', or 'S'

    computer=random.choice(["R","P","S"])

    #Prompt the user for their RPS selection

    player=input("Choose either R, P, or S:")

    #Determine winner and state what happened to the user

    if computer=="R":
      print("Computer chose rock")
    if computer=="P":
      print("Computer chose paper")
    if computer=="S":
      print("Computer chose scissors")

    if player=="R":
      print("Player chose rock")
    if player=="P":
      print("Player chose paper")
    if player=="S":
      print("Player chose scissors")

    if computer=="R" and player=="R":
      print("Tie")
      ties = ties + 1

    if computer=="R" and player=="P":
      print("Player wins! :)")
      wins = wins + 1

    if computer=="R" and player=="S":
      print("Player loses :/")
      losses = losses + 1

    if computer=="P" and player=="R":
      print("Player loses :/")
      losses = losses + 1

    if computer=="P" and player=="P":
      print("Tie")
      ties= ties + 1

    if computer=="P" and player=="S":
      print("Player wins! :)")
      wins = wins + 1

    if computer=="S" and player=="R":
      print("Player wins! :)")
      wins = wins + 1

    if computer=="S" and player=="P":
      print("Player loses :/")
      losses = losses + 1

    if computer=="S" and player=="S":
      print("Tie")
      ties= ties + 1

    #Ask the user if they would like to play again.

    playAgain=input("Do you want to play again? (Y/N):")
    
    if playAgain=="N":
      print("Thanks for playing")

    if playAgain != "N" and playAgain != "Y" and playAgain != "check score":
      input("Enter either Y or N: ")

    if playAgain== "check score":
      print("Wins \t Ties \t Losses")
      print("---- \t ---- \t ------")
      print(wins, "\t", ties , "\t", losses)
      playAgain= input("Do you want to play again? (Y/N):")
      

  
  




  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()

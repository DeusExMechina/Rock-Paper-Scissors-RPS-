import random

print("R is for rock, P for paper, S for scissors")

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None


    player = input("rock, paper, or scissors?: ").lower()

    if player is not choices:
        print("Invalid input. Try again!")
  
        
    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("It is a Tie!")
    

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            break
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            break

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            break
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            break

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
            break
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
            break


print("Bye!")

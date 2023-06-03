from random import randint

def check_args(player, computer):
    if player == computer:
        print("Tie!")
    if player == "rock":
        if computer == "scissors":
            print(player, "beats", computer, "\nYou win")
        elif computer == "paper":
            print(computer, "beats", player, "\nYou lose")
    elif player == "scissors":
        if computer == "rock":
            print(computer, "beats", player, "\nYou lose")
        elif computer == "paper":
            print(player, "beats", computer, "\nYou win")
    elif player == "paper":
        if computer == "scissors":
            print(computer, "beats", player, "\nYou lose")
        elif computer == "rock":
            print(player, "beats", computer, "\nYou win")
    else:
        print("Invalid argument")

choices = ["rock", "paper", "scissors"]
comp_choice = choices[randint(0,2)]

player_choice = input("rock, paper or scissors?\n")
check_args(player_choice, comp_choice)
git cloned

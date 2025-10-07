import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice}

    return choices

def check_win(player, computer):
    # print("You chose " + player + " Computer chose " + computer)
    print(f"You chose {player} , computer chose {computer} ")

    if player == computer:
        return "It's a tie"

    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win"
        else:
            return "Paper covers rock. You lose."
    
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock. You win"
        else:
            return "Scissors cuts paper. You lose."

    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You win"
        else:
            return "Rock smeshes scissors. You lose."

# elif player == "rock" and computer == "scissors":
#     return "Rock smashes scissors! You win"
# elif player == "rock" and computer == "paper":
#     return "Paper covers rock. You lose."

# get_choices()
# check_win("rock", "paper")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

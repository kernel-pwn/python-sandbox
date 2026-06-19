import random

options = ("rock", "paper", "scissors")

playing = True

while playing:

    player_choice = None
    computer_choice = random.choice(options)

    while player_choice not in options:
        player_choice = input("enter your choice (rock, paper, or scissors): ").lower()

    print(f"player chose {player_choice}")
    print(f"computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("draw")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win")
    else:
        print("You lose")

#   if not input("do you want to play again? (y/n): ").lower() == "y":
    play_again = input("do you want to play again? (y/n): ").lower()
    if not play_again == "y":
        playing = False
    
print("Thank you for playing")
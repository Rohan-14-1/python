import random

choices = ["rock", "paper", "scissors"]

wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid input. Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif wins[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def main():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("Congratulations, you win!")
        else:
            print("Sorry, you lose. Better luck next time!")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()

import random

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        print("\nRock, Paper, Scissors Game\n")
        print("Enter your choice: rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"\nYour choice: {user_choice}\nComputer's choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if 'You win!' in result:
            user_score += 1
        elif 'Computer wins!' in result:
            computer_score += 1
        print(f"\nYour score: {user_score}\nComputer's score: {computer_score}")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()






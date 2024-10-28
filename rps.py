import random

choices = {"1": "rock", "2": "paper", "3": "scissors"}

def get_computer_choice():
    return random.choice(list(choices.values()))

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nChoose your option: \n1. Rock\n2. Paper\n3. Scissors\nQ. Quit")
        user_input = input("Enter the number of your choice (1, 2, 3) or 'Q' to quit: ").lower()
        
        if user_input == "q":
            print("Thanks for playing!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break  # Exit the loop and end the game
        elif user_input in choices:
            user_choice = choices[user_input]
            computer_choice = get_computer_choice()
            print(f"You chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")
            result = determine_winner(user_choice, computer_choice)
            print(result)

            if result == "You win!":
                user_score += 1  # Increment user score for a win
            elif result == "Computer wins!":
                computer_score += 1  # Increment computer score for a win

            print(f"Score - You: {user_score}, Computer: {computer_score}")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 'Q' to quit.")

play_game()


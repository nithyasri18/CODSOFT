import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def display_choices_and_result(user_choice, computer_choice, result):
    print(f"Your choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    print(result)
user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    display_choices_and_result(user_choice, computer_choice, result)
    if "win" in result.lower():
        user_score += 1
    elif "computer" in result.lower():
        computer_score += 1
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
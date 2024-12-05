import random

options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
rules = {
    "Rock": ["Scissors", "Lizard"],
    "Paper": ["Rock", "Spock"],
    "Scissors": ["Paper", "Lizard"],
    "Lizard": ["Paper", "Spock"],
    "Spock": ["Rock", "Scissors"]
}

print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")

while True:
    user_input = input("Choose Rock, Paper, Scissors, Lizard, or Spock (type 'exit' to quit): ").capitalize()
    if user_input == 'Exit':
        print("Thanks for playing! Goodbye!")
        break

    if user_input not in options:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(options)
    print(f"The computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!")
    elif computer_choice in rules[user_input]:
        print(f"You won! {user_input} beats {computer_choice}.")
    else:
        print(f"You lost! {computer_choice} beats {user_input}.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break


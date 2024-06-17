# crea un gioco semplice, come sass, forbici e carta

import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return "You win!"
    elif user_choice == 'rock' and computer_choice == 'paper':
        return "You lose!"
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "You win!"
    elif user_choice == 'paper' and computer_choice == 'scissors':
        return "You lose!"
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "You win!"
    elif user_choice == 'scissors' and computer_choice == 'rock':
        return "You lose!"
    
def game():
    print("Welcome to the Rock, Paper, Scissors game!")
    print("Please pick: rock, paper or scissors.")
    
    user_choice = input()
    if user_choice in ['rock', 'paper', 'scissors']:
        print(f"You chose {user_choice}.")
    else:
        print(f"Invalid input! You have not entered rock, paper or scissors, try again.")
        game()
    
    computer_choice = get_computer_choice()
    print(f"The computer chose {computer_choice}.")

    print( get_winner(user_choice, computer_choice))

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        game()
    else:
        print("Thank you for playing!")

#game()
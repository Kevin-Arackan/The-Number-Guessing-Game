from art import logo
from random import randint
from math import floor

def confirm_input(input_string, valid_responses):
    """
    This is a function to confirm the user input
    """
    while True:
        response = input(input_string)
        if response in valid_responses:
            break
        else:
            print("\nPlease print a valid response\n")
    return response


def confirm_round():
    """
    Checks if the user wants to play a round of the number guessing game.
    Returns True if so, False otherwise.
    """
    valid_responses = ['yes', 'Yes', 'YES', 'no', 'No', 'NO']
    input_string = "Would you like to play a round of the Number Guessing Game? "
    response = confirm_input(input_string=input_string, valid_responses=valid_responses)
    if valid_responses.index(response) < 3:
        return True
    return False


def determine_mode():
    """
    Determines which mode the user wants to play in.
    Returns True if the user wants to play in Hard Difficulty, False if they want to play in Easy Difficulty.
    """
    valid_responses = ['easy', 'Easy', 'EASY', 'hard', 'Hard', 'HARD']
    input_string = "Would you like to play in easy mode or hard mode? (Type 'easy' or 'hard') "
    response = confirm_input(input_string=input_string, valid_responses=valid_responses)
    if valid_responses.index(response) > 2:
        return True
    return False


def make_a_guess(tries):
    """
    Validates a guess.
    Returns the guess.
    """
    while True:
        try:
            guess = floor(float(input(f"\nYou have {tries} tries remaining. Pick a number from 1 to 100: ")))
            if guess > 0 and guess < 101:
                return guess
        except ValueError:
            print("Please print a valid number.")   


def play_game():
    """
    Plays a round of the number guessing game.
    """
    
    # Displays the logo
    print("\n" * 100)
    print(logo)
    print("\n")
    
    # Get mode
    difficult_mode = determine_mode()
    tries = 10
    if difficult_mode:
        tries = 5
    
    # Getting a number from 1 to 100
    num = randint(1, 100)
    guess = 0
    
    while tries > 0:
        guess = make_a_guess(tries)
        if guess == num:
            print("\nCongratulations! You got it!\n")
            break
        elif guess < num and tries > 0:
            print("\nHigher.")
        elif tries > 0:
            print("\nLower.")
        tries -= 1
    
    if tries <= 0:
        print("\nYou lose.\n")
    
    
def main():
    while confirm_round():
        play_game()
    print("Goodbye!")
    
if __name__ == "__main__":
    main()
    
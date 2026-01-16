import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = poss_values[len(poss_values)//2]
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val > current_val:
        if user_input == "h":
            return True
        else:
            return False
    else:
        if user_input == "l":
            return True
        else:
            return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    if letter not in word:
        print(f"Sorry, '{letter}' is not in the word")
        return False
    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter
    print("Well done! '{}' is in the word")
    return True
        

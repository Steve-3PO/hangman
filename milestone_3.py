import random

words_list = ["banana", "kiwi", "blueberry", "tangerine", "mango"]

word = random.choice(words_list)   
    
def check_guess(choice):
    choice = choice.lower()
    if choice in word:
        print(f"Good guess! {choice} is in the word.")
    else:
        print(f"Sorry, {choice} is not in the word. Try again.")
    
def ask_for_input():
    while True:
        guess = input("Make a guess: ")
        if (guess.isalpha() == True) and (len(guess) == 1):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            
    check_guess(guess)
    
ask_for_input()
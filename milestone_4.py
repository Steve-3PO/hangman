import random

words_list = ["banana", "kiwi", "blueberry", "tangerine", "mango"]

class Hangman():
    def __init__(self, word_list, num_lives = 5) -> None:
        word = random.choice(words_list)   
        self.word = word

        self.word_guessed = [''] * len(self.word)
        
        self.num_letters = len(set([*self.word]))
        
        self.num_lives = num_lives
        
        self.word_list = word_list
        
        self.list_of_guesses = [] 
    
    def check_guess(self, choice):
        choice = choice.lower()
        if choice in self.word:
            print(f"Good guess! {choice} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == choice:
                    self.word_guessed[i] = choice
            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            print(f"Sorry, {choice} is not in the word.")
            print(f"You have {self.num_lives} lives left")
    
    
    def ask_for_input(self):
        guess = input("Make a guess: ")
        if (guess.isalpha() != True) or (len(guess) != 1):
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You have already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
                
def play_game(word_list):
        num_lives = 5
        game = Hangman(word_list, num_lives)
        while True:
            if game.num_lives == 0:
                print("You lost!")
                break
            elif game.num_letters > 0:
                print(game.word_guessed)
                game.ask_for_input()
            else:
                print("Congratulations. You won the game!")
                print(f"The word was {game.word}!")
                break
            
play_game(words_list)
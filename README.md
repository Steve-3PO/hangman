# Hangman (AiCore training)


## Overview 
> - This is an implitation of the classic Hangman game, where the computer will generate a word and the user tries to guess it within a certain amount of attempts. 

## Learning Objectives
> - To utilise OOP principles to build the game
> - To implement good python practise and coding

## Project Structure

### Milestone 1 - "Create the Variables for the Game"
> - Define list of possible words
> - Select a random word from list
> - Ask user for input
> - Validate user input

### Milestone 2 - "Check if the Guessed Character is in the Word"
> - Iteratively check for valid user input
> - Check if guess in word

### Milestone 3 - "Create the Game Class"
> - Create the class
> - Define what happens if letter is/not in word

### Milestone 4 - "Putting it all Together"
> - Code the logic of the game

## M1 - "Create the Variables for the Game"

The first variable to define is the list of words that the computer can select. In the normal game of Hangman there are no limits to what can be chosen however to test the code, a small list of 5 elements, ```word_list```, is used so that computation and testing can be swift.

To select a random word for the computer's choice we can implement the random library's function .choice() which will return the value of a random index within the list. 

```python
word = random.choice(words_list)
```

With the computer's word selected now we can begin asking for input from the user. The ```input()``` will do this easily enough. However to check that the user has entered a valid character we can implement the following code:

```python
if (guess.isalpha() == True) and (len(guess) == 1):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
```

As we want to limit the use's choice to a single alphabetical character, we use len() and .isalpha() to check for the conditions these are satisfied.

## M2 - "Check if the Guessed Character is in the Word"

Building on what we started in the previous milestone, we can iteratively check the user's input with a while loop and subsequently create a function to store this. 

```python
def ask_for_input():
    while True:
        guess = input("Make a guess: ")
        if (guess.isalpha() == True) and (len(guess) == 1):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
```

Next all we need is to check whether this character is within the word. Disregarding what happens if it is or is not in the word, we want to focus on checking this condition first.

```python
def check_guess(choice):
    choice = choice.lower()
    if choice in word:
        print(f"Good guess! {choice} is in the word.")
    else:
        print(f"Sorry, {choice} is not in the word. Try again.")
```

Here we define a function that takes in a character (choice) argument, converting it to lower case for consistency and subsequently comparing it with the computer's word. 

## M3 - "Create the Game Class"

To create a class for our Hangman game we must start with knowing what we want to initialise. We require each game instance to have a word associated with that instance. The word of the instance allows us to then create a list of blanks that the user will see when they play the game. A set which contains the letters of the word that remain unguessed, the lives of the user and the list of guesses already made.

```python
class Hangman():
    def __init__(self, word_list, num_lives = 5) -> None:
        word = random.choice(words_list)   
        self.word = word

        self.word_guessed = [''] * len(self.word)
        
        self.num_letters = len(set([*self.word]))
        
        self.num_lives = num_lives
        
        self.word_list = word_list
        
        self.list_of_guesses = []
```

These variables will be essential, as with each iteration we can see whatever the state of the game is by one look at the instance and what each parameter returns.

Now we have the Hangman Class initialised we can move our functions into this, and progress with defining what must happen when letters are/not in the generated word. 

Rather than simply printing out whether the user got the guess right or wrong, now we can make sure we modify the state of the instance to reflect this. When a guess is good, we iterate through the word and change our blank space to that letter, while remembering to reduce the ```num_letters``` (the set of letters unguessed) by 1.

```python
 def check_guess(self, choice):
        choice = choice.lower()
        if choice in self.word:
            print(f"Good guess! {choice} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == choice:
                    self.word_guessed[i] = choice
            self.num_letters -= 1
```

If the user does not guess correctly then we simply return the number of lives they have left, remembering to decrement ```num_lives``` by 1 here too. 

```python           
        else:
            self.num_lives -= 1
            print(f"Sorry, {choice} is not in the word.")
            print(f"You have {self.num_lives} lives left")
```

Now that our functions are within our Hangman class, the ```ask_for_input()``` function also changes as now we want to check each guess that is valid and append the guess to the instance's list of guesses already made, regardless if it is correct or not.

```python
def ask_for_input(self):
    while True:
        guess = input("Make a guess: ")
        if (guess.isalpha() != True) or (len(guess) != 1):
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You have already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess) 
```
            


## M4 - "Putting it all Together"







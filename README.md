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
> - Create methods for running checks
> -  Define what happens if letter is/not in word

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



## M4 - "Putting it all Together"







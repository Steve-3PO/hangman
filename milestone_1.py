import random

words_list = ["banana", "kiwi", "blueberry", "tangerine", "mango"]
print(words_list)

word = random.choice(words_list)
print(word)

guess = input("Make a guess: ")
print(guess)

if (guess.isalpha() == True) and (len(guess) == 1):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
# Project 2 — Number Guessing Game
# Author: Ada

import random

# generate a random secret number between 1 and 10
secret = random.randint(1, 10)

# set up a guesses counter
guesses = 0

# get the user's first guess
guess = int(input("Guess a number between 1 and 10: "))

# while loop — keep asking until the guess is correct
while guess != secret:
    guesses += 1

    if guess < secret:
        guess = int(input("Too low! Try again: "))
    else:
        guess = int(input("Too high! Try again: "))

# count the correct guess
guesses += 1

# print the congratulations message
print(f"Correct! You got it in {guesses} guesses.")
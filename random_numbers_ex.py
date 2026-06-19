# number guessing game

import random

lowest = 1
highest = 1000
answer = random.randint(lowest, highest)
guesses = 0
is_running = True

print("python number guessing game")
print(f"select a number between {lowest} and {highest}")

while is_running:
    guess = input("enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest or guess > highest:
            print("out of range")
            print(f"please enter a number between {lowest} and {highest}")
        elif guess < answer:
            print("too low")
        elif guess > answer:
            print("too high")
        else:
            print(f"correct! The answer was {answer}")
            print(f"you guessed {guesses} times")
            is_running = False
    else:
        print("invalid input")
        print("try again")
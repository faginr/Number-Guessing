#Guess the number game

import random
secretNumber = random.randint(1,100)
print("I am thinking of a number between 1 and 100.")

#Ask for a guess

for guessTally in range(1,7):
    print("Make a guess:")
    guess = int(input())

    if guess < secretNumber:
        print("Too Low!")
    elif guess > secretNumber:
        print("Too High!")
    else:
        break

    if guess == secretNumber:
        print("Correct! You guessed correctly in " + str(guessTally) + " guesses.")
    else:
        print("Wrong! The number was " + str(secretNumber))
        

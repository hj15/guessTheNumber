import random

randomNumber = random.randrange(1, 20)

numberOfGuesses = 0

print('I am thinking of a number between 1 and 20.')

guessIsWrong = True

def compareNumbers(guess, randomNumber):
    if(guess > randomNumber):
        print('Your guess is too high.')
    elif(guess < randomNumber):
        print('Your guess is too low.')
    else:
        print('Good job! You guessed my number in {} guesses!'.format(numberOfGuesses))
        guessIsWrong = False

while(guessIsWrong):
    numberOfGuesses += 1
    guess = int(input('Take a guess.\n'))
    compareNumbers(guess, randomNumber)






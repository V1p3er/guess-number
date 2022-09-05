import random

x = int(input("Type the number you want to guess between 1 to your number input: "))
def guess(x):
    randomNum = random.randint(1, x)
    lives = int(input("How many lives do you want to have? "))
    guesses = 0
    while guesses != randomNum and lives != 0:
        guesses = int(input(f"Guess a number between 1 and {x}: "))
        if guesses != randomNum:
            lives -= 1
        if lives == 0:
            print(f"Game Over , You couldnt guess the right number within your lives, the right number was {randomNum}")
        elif guesses == randomNum:
            print(f"You guessed right, the number was {randomNum}")
       
guess(x)

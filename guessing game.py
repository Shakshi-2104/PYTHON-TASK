import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
        break

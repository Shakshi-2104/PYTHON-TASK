import random

# Set the range for the random number
start = 1
end = 50

# Generate a random number within the range
number = random.randint(start, end)

# Loop until the user guesses correctly
print(f"Guess the number between {start} and {end}!")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
        break

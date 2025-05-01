import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Guess a number between 1 and 10!")

while True:
    # Get user input
    guess = int(input("Your guess: "))
    
    if guess == secret_number:
        print("You win! 🎉")
        # Exit Loop
        break 
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
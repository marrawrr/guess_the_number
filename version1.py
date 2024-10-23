import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Ask the user for their guess
user_guess = int(input("Guess a number between 1 and 10: "))

# Compare the user's guess to the random number
if user_guess == random_number:
    print("Congratulations! You've guessed correctly, you won!")
elif user_guess < random_number:
    print("Your guess is too low. You were incorrect.")
else:
    print("Your guess is too high. You were incorrect.")

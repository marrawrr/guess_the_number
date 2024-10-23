import random

random_number = random.randint(1, 10)

user_guess = int(input("Guess a number between 1 and 10: "))

if user_guess == random_number:
    print("Congratulations! You've guessed correctly, you won!")
elif user_guess < random_number:
    print("You were incorrect.")
else:
    print("You were incorrect.")

# Guess the Number - ALL VERSIONS

# version 1-------------------------------

# import random

# number = random.randint(1, 10)

# user_guess = int(input("Guess a number between 1 and 10: "))

# if user_guess == number:
#     print("Congratulations! You've guessed correctly, you won!")
# elif user_guess < number:
#     print("You were incorrect.")
# else:
#     print("You were incorrect.")

# version 2-------------------------------

# import random

# number = random.randint(1,10)
# print("Guess The Number Game! Play until you win!")

# print(" ")


# while True:
#   user_number=int(input("Guess the number between 1-10:"))

#   if number == user_number:
#     print("You got it!")
#     break
#   else:
#     print("Wrong number.. try again?")

# version 3-------------------------------

# import random
# counter = 1
# number = random.randint(1,10)

# print("welcome to The Guess the Number Game! You have 4 tries!")

# print(" ")

# while counter <= 4:
#   user_number=int(input("Please put a number between 1-10: "))
#   if number == user_number:
#     print("You have guessed correctly!")
#     break
#   else:
#    print("Try again!")
#   if user_number > 10:
#     print("Woah this game is 1-10!")
#   counter = counter + 1
#   if counter == 5:
#     print("You have guessed incorrectly on each attempt.")

# version 4-------------------------------

# import random
# counter = 1
# number = random.randint(1,100)
# guesses = []

# print("welcome to The Guess the Number Game! You have 4 tries.")

# print(" ")


# while counter <= 4:
#   print(f"You already guessed: {guesses}")
#   user_number = int(input("Please put a number between 1-100: "))
#   guesses.append(user_number)

#   if number == user_number:
#     print("You guessed the right number!")
#     break
#   else:
#    print("Try again")
#   counter = counter + 1

# if counter == 5:
#   print("You have failed to guessed the correct number.")

# version 5-------------------------------

# import random
# counter = 1
# number = random.randint(1,100)
# guesses = []

# print("welcome to The Guess the Number Game! You get hints and 7 tries.")
# print(" ")


# while counter <= 7:
#   print(f"You previously guessed: {guesses}")
#   user_number = int(input("Enter a number between 1-100: "))
#   guesses.append(user_number)
#   if user_number > number:
#     print("Your number is too high")
#   if user_number < number:
#     print("Your number is too low")
#   if number == user_number:
#     print("Congrats! You guessed correctly!")
#     break
#   else:
#    print("Please try again")
#   counter = counter + 1



# if counter == 7:
#   print("You have used all your guesses; therefore you lost.")

# version 6-------------------------------

import random
import os

print("Guess the Number Game!")
print(" ")

game = True
plays = 0
wins = 0

while game :
  print("*==SCOREBOARD==*")
  print(f"Games Played: {plays}")
  print(f"Games Won: {wins}")

  counter = 1
  number = random.randint(1,100)
  guesses = []


  while counter <= 8:
    print(f"You already guessed: {guesses}")
    user_number=int(input("Enter a number between 1-100: "))
    guesses.append(user_number)
    if user_number > number:
      print("Your number is greater than the chosen number.")
    if user_number < number:
      print("Your number is less than the chosen number.")
    if number == user_number:
      wins = wins + 1
      print("WooHoo! Correct!!")
      break
    else:
     print("Try again.")
    counter = counter + 1


  if counter == 7:
    print("You have used all your guesses; therefore you lost.")

  game = input("Play again to add to the score board! (y/n)? ")
  if game == "y":
    game = True
  elif game == "n":
    game = False

  plays = plays + 1
  os.system('clear')

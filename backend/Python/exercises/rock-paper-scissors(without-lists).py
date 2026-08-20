import random
import sys
# ASCII of a rock, a paper and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# User's decision

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

print(user_choice)
if user_choice == 0:
    print(rock)
elif (user_choice == 1):
    print(paper)
elif (user_choice == 2):
    print(scissors)
else:
    print("Invalid Choice")
    sys.exit("Since you didn't pick a valid choice, you lose... Maybe read better and try again")

# Computer's decision
computer_choice = random.randint(0, 2)
print("Computer chose: ")
if computer_choice == 0:
   print(rock)
elif (computer_choice == 1):
   print(paper)
elif (computer_choice == 2):
   print(scissors)

# Winning, draw and loosing conditions
if user_choice == 0 and computer_choice == 1 : # Rock vs Paper
    print("You lose...") # Rock loses
elif (user_choice == 0 and computer_choice == 2): # Rock vs Scissors
    print("You win !") # Rock wins
elif (user_choice == 1 and computer_choice == 0): # Paper vs Rock
    print("You win !") # Paper wins
elif (user_choice == 1 and computer_choice == 2): # Paper vs Scissors
    print("You lose...") # Paper loses
elif (user_choice == 2 and computer_choice == 0): # Scissors vs Rock
    print("You lose...") # Scissors loses
elif (user_choice == 2 and computer_choice == 1): # Scissors vs Paper
    print("You win !")
else :# If they both pick the same
    print("It's a draw !")




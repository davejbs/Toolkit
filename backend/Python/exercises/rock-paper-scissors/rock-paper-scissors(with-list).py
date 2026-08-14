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
# Both parties' choices
choices = [rock, paper, scissors]

# User's decision
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(user_input)
if user_input == 0:
    user_choice = choices[0]
    print(rock)
elif user_input == 1:
    user_choice = choices[1]
    print(paper)
elif user_input == 2:
    user_choice = choices[2]
    print(scissors)
else:
    print("Invalid choice\nSince you didn't pick a valid choice, you lose... Maybe read better and try again")
    sys.exit()

# Computer's decision
computer_choice = random.choice(choices)
print(f"Computer chose: \n {computer_choice}")

# Winning, draw and loosing conditions
if user_choice == rock and computer_choice == paper :
    print("You lose...")
elif user_choice == rock and computer_choice == scissors:
    print("You win !")
elif user_choice == paper and computer_choice == rock:
    print("You win !")
elif user_choice == paper and computer_choice == scissors:
    print("You lose...")
elif user_choice == scissors and computer_choice == rock:
    print("You lose...")
elif user_choice == scissors and computer_choice == paper:
    print("You win !")
else :# If they both pick the same
    print("It's a draw !")

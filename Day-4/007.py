import random

# ASCII art for rock, paper, and scissors
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
---'    ____)____
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

game_images = [rock, paper, scissors]
# print(rock)
# print(paper)
# print(scissors)

user_choice =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# 0, 1, 2
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computer chose:")
# print(f"Computer choose {computer_choice}")
print(game_images[computer_choice])

if user_choice>=3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice ==2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice < user_choice:
    print("You win!")
elif computer_choice == 0 and user_choice ==0:
    print("It's a draw!")

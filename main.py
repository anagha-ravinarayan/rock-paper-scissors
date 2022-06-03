import random

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

game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 0 and choice <= 2:
  print(f"You chose \n {game_images[choice]}")
  
  computers_choice = random.randint(0,2)
  print(f"Computer chose \n {game_images[computers_choice]}")
  
  if choice == computers_choice:
    print("You have a draw.")
  elif choice == 0 and computers_choice == 1:
    print("You lost 🙁")
  elif choice == 0 and computers_choice == 2:
    print("You won 😁")
  elif choice == 1 and computers_choice == 0:
    print("You won 😁")
  elif choice == 1 and computers_choice == 2:
    print("You lost 🙁")
  elif choice == 2 and computers_choice == 0:
    print("You lost 🙁")
  elif choice == 2 and computers_choice == 1:
    print("You won 😁")
else:
  print("Please choose a valid option.")
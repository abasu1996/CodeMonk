'Rock Paper Scissors Game'
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
user_input = input("Enter 0 for Rock, 1 for Paper and 2 for Scissors ")
game = [rock,paper,scissors]
if user_input == "0":
    print(f"You chose Rock\n{rock}")
elif user_input == "1":
    print(f"You chose Paper\n{paper}")
elif user_input == "2":
    print(f"You chose Scissor\n{scissors}")

random_input = str(random.randint(0,2))
if (random_input == "0" and user_input == "2"):
    print(f"Computer chose Rock\n{rock}... You LOSE")
elif (random_input == "0" and user_input == "1"):
    print(f"Computer chose Paper\n{paper}... You WIN")
elif (random_input == "1" and user_input == "0"):
    print(f"Computer chose Paper\n{paper}.. You LOSE")
elif (random_input == "1" and user_input == "2"):
    print(f"Computer chose Paper\n{paper}...You WIN")
elif (random_input == "2" and user_input == "0"):
    print(f"Computer chose Scissor\n{scissors}... You WIN")
elif (random_input == "2" and user_input == "1"):
    print(f"Computer chose scissor\n{scissors}..You LOSE")
elif random_input == user_input:
    print(f"Computer chose {game[int(random_input)]} It's a Draw")
else:
    print("You typed and Invalid number... YOU LOSE")
print(random_input)
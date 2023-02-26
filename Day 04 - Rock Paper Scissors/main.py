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

#Write your code below this line 👇
human = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors \n"))

list = [rock,paper,scissors]

computer = random.randint(0, 2)

if human >=3:
  print("Wrong entry, you lose!")
else:
  print(list[human])
  print(list[computer])  
  if human == computer:
      print("Draw!")
  elif human == 0 and computer == 1:
      print("Computer wins!")
  elif human == 0 and computer == 2:
      print("You won!")
  
  if human == 1 and computer == 0:
      print("You won!")
  
  elif human == 1 and computer == 2:
      print("Computer wins!")
  
  if human == 2 and computer == 0:
      print("Computer wins!")
  elif human == 2 and computer == 1:
      print("You won!")
  

import art
from random import choice
from game_data import data
from replit import clear

result = "correct"
score =0

def compare(a_followers, b_followers, user_choice):
    if user_choice == "a" and a_followers > b_followers:
        return "correct"
    elif user_choice == "b" and b_followers > a_followers:
        return "correct"
    else:
        clear()
        print(art.logo)
        return "You Lost"

while result =="correct":
  clear()
  print(art.logo)
  if score ==0:
    a = choice(data)
  else:
      print(f"You're right! your current score is:{score} \n")
  #print chosen dictionary: name decriptionn and country
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
  # print(f"Followers: {a['follower_count']}M")
  
  a_followers = a['follower_count']
  #print vs
  print(art.vs)
  b = choice(data)
  
  while a == b:
      b = choice(data)
  
  #print chosen dictionary: name decriptionn and country
  print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
  # print(f"Followers: {b['follower_count']}M")
  b_followers = b['follower_count']
  
  user_choice = input("\n Who has more followers? Type 'A' or 'B': ").lower()
  
  a=b
  result= compare(a_followers,b_followers,user_choice)
  if result == "correct":
    score +=1

clear()
print(art.logo)
print(f"\n {result}, your final score is:{score}")



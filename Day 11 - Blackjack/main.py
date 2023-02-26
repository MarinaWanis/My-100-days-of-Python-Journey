import random
from replit import clear

def draw_cards():
  """Draws random cards from the deck"""
  cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

def calculate_score(card_list):
  """Returns the sum of the cards that are drawn"""
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0
  if sum(card_list)> 21 and 11 in card_list:
    card_list.remove(11) # you can remove an item from a list
    card_list.append(1) # and replace it with append
    return(sum(card_list)) #Lerned you can use sujm to add ints in a list
  else:  
    return sum(card_list)
    
def compare_scores(user_final_score, computer_final_score):
  """Returns the final result after comparison"""
  if user_final_score >21 and computer_final_score >21:
    return "You went over 21, you lost"
  elif user_final_score > 21:
    return "You went over 21, you lost"
  elif computer_final_score >21:
    return "Computer went over 21, You won!"
  elif user_final_score == computer_final_score:
    return "Draw"
  elif user_final_score > computer_final_score:
    return "You win!"
  elif computer_final_score > user_final_score:
    return "Computer wins"   
  
def play_game():  
  """Call function to play the game"""
  user_cards= []
  computer_cards= []
  is_game_over = False
  for _ in range(2):
    user_cards.append(draw_cards())
    computer_cards.append(draw_cards())
  
  user_score = calculate_score(user_cards)  
  computer_score = calculate_score(computer_cards)
  print(user_cards, user_score)
  print(computer_cards[0])
  
  while not is_game_over:
    if sum(user_cards)>21 or user_score==0 or computer_score==0:
      is_game_over = True
    else:  
      user_want_to_continue =input("Do you want to draw another card? ")
      if user_want_to_continue == "y":
        user_cards.append(draw_cards())
        user_score = calculate_score(user_cards)  
        print(user_cards, user_score)
        print(computer_cards[0])
      else:
        is_game_over= True
        
  
  while computer_score <17:
    computer_cards.append(draw_cards())
    computer_score = calculate_score(computer_cards)

  print(f"final {user_cards}, {user_score}")
  print(f"final {computer_cards}, {computer_score}")
  print(compare_scores(user_score,computer_score)) 


#This is the recursion function
while input("Do you want to play the blackjack game? ")=="y":
  clear()
  play_game() 

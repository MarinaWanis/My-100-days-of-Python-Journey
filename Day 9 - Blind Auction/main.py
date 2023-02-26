from replit import clear
#HINT: You can call clear() to clear the output in the console.
import Auction_art

print(art.logo)
print("Welcome to the Blind Auction")

more = "yes"
bid_dict={}

while more == "yes":
  name = input("What is your name? ").lower()
  bid= int(input("What is your bid? $"))
  more = input("Are there more bidders? Yes/No: ").lower()
  clear()
  bid_dict[name]=bid

print(bid_dict)
highest_bid=0
for key in bid_dict:
  if highest_bid < bid_dict[key]:
    highest_bid = bid_dict[key]
    username = key

print(f"Congrats {username} you bid {highest_bid} was the winner!")    
  




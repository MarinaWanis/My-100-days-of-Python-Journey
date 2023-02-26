#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# total_char = nr_letter + nr_numbers + nr_symbols

random_letters=""
random_numbers=""
random_symbols=""

for randomL in range(0, nr_letters):
  random_letters_index = random.randint(0, len(letters)-1)
  # assigning the random chosen letter index(randome)to variable l
  random_letters= letters[random_letters_index] + random_letters



for randomN in range(0, nr_numbers):
  random_number_index = random.randint(0, len(numbers)-1)
  random_numbers = numbers[random_number_index] + random_numbers
 
                                  
for randomS in range(0, nr_symbols):
  random_symbol_index = random.randint(0, len(symbols)-1)
  random_symbols = symbols[random_symbol_index] + random_symbols 

final_password = random_letters + random_numbers + random_symbols

# random_password = "".join(random.sample(final_password,len(final_password)))
list_password=[]
for n in range(0,len(final_password)):
  list_password.append(final_password[n])

print(final_password)
print(list_password)
random_password =""

random.shuffle(list_password)

for n in range(0,len(list_password)):
  random_password += list_password[n]

print(f"Your password is: {random_password }")

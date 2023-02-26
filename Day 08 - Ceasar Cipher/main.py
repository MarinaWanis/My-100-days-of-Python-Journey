from ceasar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text=""
shift=""
direction=""

encoded_list=[]
decoded_list=[]
try_again ="y"


text_list=[]

print(logo)

# while try_again == "Y":
#   counter=0
#   text_list=[]
#   encoded_list=[]
#   decoded_list=[]
  
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))

  
#   for letter in text:
#     text_list += text[counter]
#     counter +=1
#   def encrypt(t, s):
#     for text_index in range (0, len(text_list)):
#       for alphabet_index in range(0,len(alphabet)):
#         if text_list[text_index] == alphabet[alphabet_index]:
#           # print(alphabet[alphabet_index],alphabet[alphabet_index+s])
#           if alphabet_index+s > 25:
#             alphabet_index =-1
#           encoded_list.append(alphabet[alphabet_index+s])
#       if text_list[text_index] not in alphabet:
#         encoded_list.append(text_list[text_index])
        
#     print("The encoded text is: "+''.join(encoded_list))
  
#   def decrypt(t,s):
#     for text_index in range(0,len(text_list)):
#       for alphabet_index in range(0, len(alphabet)):
#         if text_list[text_index] == alphabet[alphabet_index]:
#           if alphabet_index-s>25:
#             alphabet_index=1
#           decoded_list.append(alphabet[alphabet_index-s])
#       if text_list[text_index] not in alphabet:
#         decoded_list.append(text_list[text_index])
#         # print("Not in alphabet: " + text_list[text_index])
#     print("The decoded text is: "+ ''.join(decoded_list)) 
#   if direction == "encode":
#     encrypt(t=text, s=shift)
#   elif direction =="decode":
#     decrypt(t=text, s=shift)
#   try_again = input("Do you want to continue? Y or N")      
    

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


while try_again == "y":
  counter=0
  text_list=[]
  ceasar_list=[]
  new_position =0
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  user_text = input("Type your message:\n").lower()
  user_shift = int(input("Type the shift number:\n"))

  
  for letter in user_text:
    text_list += user_text[counter]
    counter +=1

  def ceasar(text,shift,type):
    # for text_index in range(0,len(text_list)):
    #   for alphabet_index in range(0,len(alphabet)):
    #     if text_list[text_index] == alphabet[alphabet_index]
          # if type == "encode":
          #   if alphabet_index + shift > 25:
          #     alphabet_index=-1
          #   ceasar_list.append(alphabet[alphabet_index+shift]) 
            
          # if type == "decode":
          #   if alphabet_index-shift >25:
          #     alphabet_index =1
          #   ceasar_list.append(alphabet[alphabet_index-shift])

    shift %= 26
    for letter in text:
      new_shift = shift
      if letter not in alphabet:
        ceasar_list.append(letter)
      else:  
        position = alphabet.index(letter)
        if type =="decode":
          new_shift = shift *-1
        new_position = position + new_shift  
        if new_position > 25: 
          print(f"new_position: {new_position} > 25")
          new_position %=26   
        # print(f"shift: {shift}, position: {position}, new_position: {new_position}")
        ceasar_list.append(alphabet[new_position])

      
    print(f"The {type}d text is: "+ ''.join(ceasar_list))  

  ceasar(text=user_text,shift=user_shift,type=direction)
  try_again = input("Do you want to continue? Y or N \n").lower()  
print("Goodbye")

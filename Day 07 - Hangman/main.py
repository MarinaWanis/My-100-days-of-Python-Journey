#Step 1 
import hangman_art
import hangman_words
import random
from replit import clear



print("Welcome to the hangman game!")
print(hangman_art.logo)

# Randomly choosing a word from the list in hangman_words module
chosen_word = random.choice(hangman_words.word_list)
lives = 6

underscore ="_"
display= []

# looping through the number of letters 
for letter in range(0,len(chosen_word)):
  display.append(underscore)

# displaying the blanks with the number of letters in the chosen word
print(display)

# setting the number of letters in the word in guessed_all variable 
guessed_all =len(chosen_word)
hangman ="True"
guessed_letters =[]

# loop as long as there are lives left or when there are more letters to guess
while (lives>0) and (guessed_all>0): #or guessed_all>0:
  hangman ="True"
  print(f"\n Letters left:{guessed_all}, Lives left: {lives}")

  # Inputing the letter guessed
  guess = input("\n Guess a letter: ").lower()
  clear()

  # If ltter doesn't exist in the chosen word
  if guess not in guessed_letters:
    # just append the letter in a variable so that when guessed again the user will know
      guessed_letters.append(guess)
      # looping thourgh each letter in the chosen word 
      for index in range(0,len(chosen_word)):
        # if the letter guessed exist in the word, then remove the blank from the display and replace it with the letter guessed
        if guess == chosen_word[index]:
            display[index] = guess
            # set it to false so that user doesn't lose a life 
            hangman = "False"
            guessed_all -= 1 # or if "_" not in display
      # If the letter doesn't exist in any of the leters in the word, lose a life    
      if hangman == "True":
        print(f"You have guessed {guess}, that's not in the word. You lost a life")
        lives -= 1
        # printing the hangman
      print(hangman_art.stages[lives])
  else:
    print(f"Oops, you have entered {guess} letter twice!")
  # printing display in a string format
  print(f"\n {' '.join(display)}")
  
if guessed_all == 0:  
  print(f"The word is: {chosen_word}")
  print("\n \n You win!")  
elif lives == 0:
  print(f"The word is: {chosen_word}")
  print("\n \n You lost")


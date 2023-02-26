#Calculator

from replit import clear
from calculator_art import logo

#Addtition
def add(n1,n2):
  return n1+n2
  
#Subtract
def subtract(n1,n2):
  return n1-n2
  
#Multiple
def multiply(n1,n2):
  return n1*n2
  
#Divide
def divide(n1,n2):
  return n1/n2

#Dictionary
operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  print(logo)
  num1= float(input("What's the first number?: "))

  for symbol in operations:
    print(symbol)
  
  continue_cal = "y"

  while continue_cal== "y":
    operation_symbol= input("Chooe one of the operators above: ")
    num2= float(input("What's the second number?: "))
    function =operations[operation_symbol]
    answer = function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer},")
    num1 = answer
    continue_cal = input(f"Do you want to continue with {num1}, y/n/again: ")
    if continue_cal == 'again':
      clear()
      calculator()

      
calculator()  
clear()
print("Thanks for using our calculator")  





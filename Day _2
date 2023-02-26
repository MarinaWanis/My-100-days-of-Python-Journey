#Day 2 - Tip Calculator
print("Welcome to the tip Calculator")
total_bill = input("What was the total bill? $")
tip_percentage = input(
    "What percentage tip would you like to give? 10, 12, or 15? ")
num_of_people = input("How many poeple to split the bill? ")

float_total_bill = float(total_bill)
int_tip_plus_total_bill = float_total_bill + float_total_bill * (
    int(tip_percentage) / 100)

#rounding to 2 decimal places with formating issue like displaying 33.6 instead of 33.60
int_each_person = round(int_tip_plus_total_bill / int(num_of_people), 2)

bill_per_person = float(int_tip_plus_total_bill) / int(num_of_people)

#another way of rounding to 2 decimal palaces without formating12 issue
total_bill = "{:.2f}".format(bill_per_person)

outcome = f"Each person should pay: ${total_bill}"
print(outcome)

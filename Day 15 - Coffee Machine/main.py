MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money =0
want_drink = True

while want_drink:
    exit_loop = False
    drink = ""
    # TODO: 1 prompt - What would you like? (espresso/latte/cappuccino):
    users_input = input("What would you like: (e-espresso/ l-latte/ c-cappuccino): ").lower()

    # TODO: 2 prompt - off will switch off the coffee machine

    # TODO: 3: prompt - report will print the report of current resources
    if users_input == "report":
        print(f"Coffee: {resources['coffee']}g")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: S{money}")

    if users_input == "off":
        break

    if users_input == "e":
        drink = "espresso"
    elif users_input == "l":
        drink = "latte"
    elif users_input == "c":
        drink = "cappuccino"

    exit_loop = False
    if drink != "":
        # TODO: 5: when user asks for drink, machine will check the ingredients against resources
        water_left = resources["water"] - MENU[drink]["ingredients"]["water"]
        # TODO: 4: check the if resources are enough or not
        if water_left < 0:

            print(f"There isn't enough water in the machine, sorry can't make your {drink}.")
            continue
        else:
            resources["water"] = water_left

        coffee_left = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
        if coffee_left < 0:
            print(f"There isn't enough coffee in the machine, sorry can't make your {drink}.")
            continue
        else:
            resources["coffee"] = coffee_left

        if drink != "espresso":
            milk_left = resources["milk"] - MENU[drink]["ingredients"]["milk"]
            if milk_left < 0 or exit_loop:
                print(f"There isn't enough milk in the machine sorry can't make your {drink}.")
                continue
            else:
                resources["milk"] = milk_left

        # TODO: when user inserts money, machine will add coins and check against the price of the drink
        if not exit_loop:
            price = MENU[drink]["cost"]
            print(f"Please insert coins. Total amount: ${price}")
            quarters = round(int(input("How many quarters?: ")) * 0.25, 2)
            dims = round(int(input("How many dims?: ")) * 0.10, 2)
            nickels = round(int(input("How many nickels?: ")) * 0.05, 2)
            pennies = round(int(input("How many pennies?: ")) * 0.01, 2)
            total_paid = round(quarters + dims + nickels + pennies, 2)
            change = round(total_paid - price, 2)
            # print(f"total paid: {total_paid} and price: {price} and change: {change}")
            if change < 0:
                print(f"That's not enough money for the {drink}. Money Refunded")
            elif change == 0:
                print(f"You have paid: {total_paid}.")
                print(f"Here is your {drink} ☕️. Enjoy!")
                money += price
            else:
                print(f"You have paid: {total_paid}, your change is: {change}.")
                print(f"Here is your {drink} ☕️. Enjoy!")
                money += price
"""If machine have enough resources and the money inserted is enough:
then the machine will process by subtracting from resources and adding the money """

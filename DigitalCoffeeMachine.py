
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

def report_resources():
    for i,j in resources.items():
                if i.lower() in ["water","milk"]:
                    print(f"{i.title()}: {j}ml")
                if i.lower() == "coffee":
                    print(f"{i.title()}: {j}g")
                if i.lower() == "money":
                    print(f"{i.title()}: {j}$")


def total_amount(quarters, dimes, nickles, pennies):
    return (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (0.01*pennies)


def check_coffee_money(quarters, dimes, nickles, pennies, type):
    money = total_amount(quarters, dimes, nickles, pennies)

    if type == "latte" and money >= 2.50:
        return (True,round(money - 2.50,2))
    elif type == "cappuccino" and money >= 3.00:
        return (True,round(money - 3.00,2))
    elif type == "espresso" and money >= 1.50:
        return (True,round(money - 1.50,2))
    
    return (False,0)


def sufficient_ingredients(type):
    if type == "latte":
        if resources["water"] >= 200:
            if resources["coffee"] >= 24:
                if resources["milk"] >= 150:
                    return (True,0)
                return False,"milk"
            return False,"coffee"
        return False,"water"
    
    elif type == "cappuccino":
        if resources["water"] >= 250:
            if resources["milk"] >= 100:
                if resources["coffee"] >= 24:
                    return True,0
                else: 
                    return False,"coffee"
            else:
                return False,"milk"
        else:
            return False,"water"
    
    elif type == "espresso":
        if resources["water"] >= 50:
            if resources["coffee"] >= 18:
                return True,0
            else:
                return False,"coffee"
        else:
            return False,"water"
    
def add_resources(milk, water, coffee):
    resources["milk"] += milk
    resources["water"] += water
    resources["coffee"] += coffee


def adjust_resources(type):
    if type == "latte":
        resources["water"] -= 200
        resources["coffee"] -= 24
        resources["milk"] -= 150
    
    elif type == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
    
    elif type == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18

logo = r"""


   ______      ________             __  ___           __    _          
  / ____/___  / __/ __/__  ___     /  |/  /___ ______/ /_  (_)___  ___ 
 / /   / __ \/ /_/ /_/ _ \/ _ \   / /|_/ / __ `/ ___/ __ \/ / __ \/ _ \
/ /___/ /_/ / __/ __/  __/  __/  / /  / / /_/ / /__/ / / / / / / /  __/
\____/\____/_/ /_/  \___/\___/  /_/  /_/\__,_/\___/_/ /_/_/_/ /_/\___/ 
                                                                       


"""

def start():
    transactions = 0
    money = 0

    print(logo)

    while(True):
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        print()
        choice = choice.lower()

        if choice == "report":
            report_resources()
            print(f"Money: ${money}")
            print(f"Transactions: {transactions}")
            print()

        elif choice == "off":
            break

        elif choice == "add":
            milk = int(input("Milk: "))
            water = int(input("Water: "))
            coffee = int(input("Coffee: "))
            add_resources(milk, water, coffee)

        elif choice in ["latte","cappuccino","espresso"]:

            ingredient_check = sufficient_ingredients(choice)
            if not ingredient_check[0]:
                print(f"Sorry, not enough {ingredient_check[1]}.")
                print("Please come back later.")
                print()
                continue
            
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            money_given = total_amount(quarters, dimes, nickles, pennies)
            print()

            order = [ingredient_check,check_coffee_money(quarters, dimes, nickles, pennies, choice)]
            
            print(f"You gave amount {round(money_given,2)}")
            print()
            if order[0][0] and order[1][0]:
                transactions += 1
                if order[1][1] > 0:
                    print(f"Here is ${order[1][1]} dollars in change")
                print(f"Here is your {choice}. Enjoy!")
                adjust_resources(choice)
                if choice == "latte":
                    money += 2.5
                elif choice == "cappuccino":
                    money += 3
                elif choice == "espresso":
                    money += 1.5
            
            elif not order[1]:
                print(f"Sorry, that's not enough money. Money Refunded.")
                print(f"Money refunded ${round(money_given,2)} dollars")
            
        print()
                

start()


             
        
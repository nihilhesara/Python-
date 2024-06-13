# Initialize variables
Water = 300
Milk = 200
Coffee = 100
Money = 0

# Function to calculate price
def coin_count(quarters,dimes,nickles,pennies,price,choice):
    quarters = quarters * 0.25
    dimes = dimes * 0.1
    nickles = nickles * 0.05
    pennies = pennies * 0.01

    total = quarters + dimes + nickles + pennies

    change = total - price

    if (change > 0):
        print(f"Here is {change} in change.")
        print(f"Here is your {choice}. Enjoy!")
        
    else:
        print("Sorry that's not enough money. Money refunded.")


while True:
    choice = input(" What would you like? (espresso/latte/cappuccino) : ")

    if (choice.lower() == "espresso"):
        print()
    elif (choice.lower() == "latte"):
        print()
    elif (choice.lower() == "cappuccino"):
        print()
    elif (choice.lower() == "report"):
        print()

   
        
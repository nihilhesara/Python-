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

    # Calculate total and change 
    total = quarters + dimes + nickles + pennies
    change = total - price
    round(change , 2)

    if (change > 0):
        print(f"\nHere is {change} in change.")
        print(f"Here is your {choice}. Enjoy!\n")
        return price
        
    else:
        print("Sorry that's not enough money. Money refunded.")
      
while True:
    choice = input("What would you like? (espresso/latte/cappuccino) : ")

    # User report
    if (choice.lower() == "report"):
        print(f"\nWater : {Water}ml")
        print(f"Milk : {Milk}ml")
        print(f"Coffee : {Coffee}g")
        print(f"Money : ${Money}")
        continue

    elif (choice.lower() == "off"):
        exit()
    
    # Getting inputs for the coins 
    quarters = int(input("How many quarters : "))
    dimes = int(input("How many dimes : "))
    nickles = int(input("How many nickles : "))
    pennies = int(input("How many pennies : "))

    # Main program according to the user choice 
    if (choice.lower() == "espresso"):
        price = 1.5
        
        if (Water < 50):
            print("Sorry there is not enough water.")
        elif (Coffee < 18):
            print("Sorry there is not enough Coffee.")
        else:
            coin_count(quarters,dimes,nickles,pennies,price,choice)

        Water -= 50
        Coffee -= 18
        Money += price

    elif (choice.lower() == "latte"):
        price = 2.5

        if (Water < 200):
            print("Sorry there is not enough water.")
        elif (Milk < 150):
            print("Sorry there is not enough Milk.")
        elif (Coffee < 24):
            print("Sorry there is not enough Coffee.")
        else:
            coin_count(quarters,dimes,nickles,pennies,price,choice)
        
        Water -= 200
        Milk -= 150
        Coffee -= 24
        Money += price
        

    elif (choice.lower() == "cappuccino"):
        price = 3
        
        if (Water < 250):
            print("Sorry there is not enough water.")
        elif (Milk < 100):
            print("Sorry there is not enough Milk.")
        elif (Coffee < 24):
            print("Sorry there is not enough Coffee.")
        else:
            coin_count(quarters,dimes,nickles,pennies,price,choice)
        
        Water -= 250
        Milk -= 100
        Coffee -= 24
        Money += price

    else:
        print("Error!")    
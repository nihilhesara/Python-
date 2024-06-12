# Initilizing variables
final_bill = 0

print("Thank you for choosing Python Pizza Deliveries!")

# Adding price for the size
size = input() 
if (size.lower == "s"):
    final_bill += 15
elif (size.lower == "m"):
    final_bill += 20
else:
    final_bill += 25

# Adding price for the pepperoni
add_pepperoni = input() 
if (add_pepperoni.lower == "y"):
    final_bill += 2

# Adding price for extra cheese
extra_cheese = input()
if (extra_cheese.lower == "y"):
    final_bill += 1

print(f"Your final bill is: ${final_bill}.")
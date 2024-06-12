# Welcome message 
print("Welcome to the tip calculator.")

# Getting user inputs
total_bill = input("What was the total bill? : ")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? : ")  
people_split = input("How many people to split the bill? : ")

# Converting user inputs to float
total_bill_float = float(total_bill)
tip_percentage_float = float(tip_percentage)  
people_split_float = float(people_split)

# Calculating tip amount
tip_percentage_float_result = (tip_percentage_float / 100)
total_bill = total_bill_float + (total_bill_float * tip_percentage_float_result)
each_person_pay = round(total_bill / people_split_float , 2)

# Printing result
print(f"Each person should pay : {each_person_pay} ")

# Getting Inputs
height = float(input("Enter your height in (kg) : "))
weight = float(input("Enter your weight in (m) : "))

# Calculating BMI
BMI = weight / (height * height)

# Round BMI for two decimals
round(BMI , 2)

# Giving Output
print(f"Your BMI is {BMI} ")
# Getting Inputs
height = float(input("Enter your height in (m) : "))
weight = float(input("Enter your weight in (kg) : "))

# Calculating BMI
BMI = weight / (height * height)

# Round BMI for two decimals
round(BMI , 2)

# Giving Output
if (BMI < 18.5):
    print(f"Your BMI is {BMI}, you are underweight.")
elif (BMI < 25):
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif (BMI < 30):
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif (BMI < 35):
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
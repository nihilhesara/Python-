# Getting inputs from the user
year = int(input("Enter the year you want to convert : "))

# Check the year is a leap year or not a leap year
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")
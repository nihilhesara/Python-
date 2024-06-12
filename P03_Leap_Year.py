year = int(input("Enter the year you want to convert : "))

if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")
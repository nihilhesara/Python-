import os
import pandas             # python -m pip install pandas

os.chdir(os.path.dirname(os.path.abspath(__file__)))    # move file path to the woking folder

'''with open ("weather_data.csv") as data_file:
    data = data_file.readlines()                        # readlines get each line in the csv file and turn it into a list
    print(data)

import csv                # open cmd and type this code below

with open ("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    
    temperatures = []
    # to print each item in the csv folder as a list we have to loop through each row and print it 
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)'''

data = pandas.read_csv("weather_data.csv")
print(data)
print("\n\n")
print(data["temp"])
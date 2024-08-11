import os
import pandas             # python -m pip install pandas (pandas documentation - https://pandas.pydata.org/docs/reference/index.html)

os.chdir(os.path.dirname(os.path.abspath(__file__)))    # move file path to the woking folder

'''with open ("weather_data.csv") as data_file:         # https://docs.google.com/spreadsheets/d/1Rs1CKjiagTeXa53212JkjRSDu-tx77_YxEgGdkv5zRY/edit?gid=0#gid=0
    data = data_file.readlines()                        # click the above google sheet link and download it as a csv file                        
    print(data)                                         # readlines get each line in the csv file and turn it into a list

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
print(data["temp"])                         # List is like a series in pandas library
# but tables are data frames like 2d arrayes in java
temp_list = data["temp"].to_list()                      # convert data to a list
print(len(temp_list))

# Getting the average temp
average = sum(temp_list) / len(temp_list)
print(average)

# Short method to get the average 
print(data["temp"].mean())                  # dataframe[column name].method name

# to find the maximum temp
print(data["temp"].max())

# Get data in a row
print(data[data.day == "Monday"])

# get the max temp row 
print(data[data.temp == data.temp.max()])

# Getting monday temp and convert it in to farenheit
monday = data[data.day == "Monday"]
print(monday.temp * (9/5) + 32) 

# Create datafram from scratch
data_dict = {
    "students" : ["Amy","James","Angela"],
    "scores" : [75,65,55]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)

# Create a new CSV file from new data
data_frame.to_csv("new_data.csv")
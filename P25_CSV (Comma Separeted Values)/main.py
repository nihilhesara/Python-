import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))    # move file path to the woking folder

'''with open ("weather_data.csv") as data_file:
    data = data_file.readlines()                        # readlines get each line in the csv file and turn it into a list
    print(data)'''

with open ("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    
    # to print each item in the csv folder as a list we have to loop through each row and print it 
    for row in data:
        print(row)
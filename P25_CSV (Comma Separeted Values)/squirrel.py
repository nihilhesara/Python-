import pandas
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

data = pandas.read_csv("Squirrel_Data.csv")
print(data)
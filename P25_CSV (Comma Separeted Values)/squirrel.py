import pandas 
import os

# Initialize counters for each color
Grey = 0
Cinnamon = 0
Black = 0

# Change directory to the location of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read CSV data into a DataFrame
data = pandas.read_csv("Squirrel_Data.csv")

# Filter and count occurrences for each fur color
Grey = len(data[data.Primary_Fur_Color == "Gray"])          # Use len function to count thr squirrels
Cinnamon = len(data[data.Primary_Fur_Color == "Cinnamon"])
Black = len(data[data.Primary_Fur_Color == "Black"])

# Print the result
print(f"Grey: {Grey}, Black: {Black}, Cinnamon: {Cinnamon}")

# Crate a dict using the counts
data_dict = {
    "Fur_Color" : ["Gray","Cinnamon","Black"],
    "Count" : [Grey,Cinnamon,Black]
}

# Convert dict into a csv file 
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
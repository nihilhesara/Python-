# method - I

file = open("file.txt")
contents = file.read()
print(contents)
file.close()

# method - II

with open("file.txt") as file:
    contents = file.read()
    print(contents)

# _________________________________________

# write mode 

with open("file.txt","w") as file:
    file.write("New text")

# __________________________________________

# append mode 
with open("file.txt","a") as file:
    file.write("\nNew text")
# method - I

file = open("/Users/ASUS/Desktop/Udemy Python/Projects/Python-/P24_Files/file.txt")
contents = file.read()
print(contents)
file.close()

# method - II

with open ("/Users/ASUS/Desktop/Udemy Python/Projects/Python-/P24_Files/file.txt") as file:
    contents = file.read()
    print(contents)

# _________________________________________

# write mode 

with open("/Users/ASUS/Desktop/Udemy Python/Projects/Python-/P24_Files/file.txt","w") as file:
    file.write("New text")

# __________________________________________

# append mode 
with open("/Users/ASUS/Desktop/Udemy Python/Projects/Python-/P24_Files/file.txt","a") as file:
    file.write("\nAppend text")
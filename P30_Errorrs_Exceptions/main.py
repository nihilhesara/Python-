# FileNotFound Error

try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["abcdef"])

except(FileNotFoundError):
    file = open("a_file.txt" , "w")
    file.write("Something")

except KeyError as error_message:   # Error message plus our message 
    print("That key does not exist")

else:
    content = file.read()
    print("Content")
    print("This will print when the code is perfectly run without an error")

finally:
    file.close()
    print("File was closed")
    print("This will run if there is an error or not")
    raise KeyError          # Programmer madup errors

#___________________________________________________________________________

# KeyError

# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

#___________________________________________________________________________

# IndexError

# fruit_list = ["Apple","Banana","Pear"]
# fruit = fruit_list[3]

#___________________________________________________________________________

# TypeError

# text = "abc"
# print(text + 5)

#___________________________________________________________________________

# raise example

height = float("Enter height : ")
weight = float("Enter weight")

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
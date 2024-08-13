# Nomal List

numbers = [1,2,3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

# _________________________________________________________________________________________

# List comprehension (Create a new list using a corrent list) - This is unique to python

numbers = [1,2,3]
new_list = [n+1 for n in numbers]
# new list name = [what you do inside the loop || for || increment variable || list name]
print(new_list)

name = "Nihil"
list_1 = [letter for letter in name]
print(list_1) 

# print 2,4,6,8 using range keyword
list_2 = [n*2 for n in range(1,5)]
print(list_2)

# _________________________________________________________________________________________

# Conditioal List Comprehension - This is unique to python

# new_list = [new_item for item in list if test]
# new list name = [what you do inside the loop if condition is True || for || increment variable || list name || if condition]

# print 4 leter names in the list using Conditioal List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Feddie"]

short_names = [name for name in names if len(name) == 4]
print(short_names)

# convert more than 4 letters in the name to uppercase

long_names = [n.upper() for n in names if len(n) >= 5]
print(long_names)
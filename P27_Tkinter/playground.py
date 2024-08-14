# Create a function that can take any numberof inputs
def add(*args): # put * to say there are multiple values and args is a variable you can change it to anything you want
    sum = 0     # This keeps every input as a tuple
    for n in args:  # So we loop through the tuple and do what we want to do 
        sum += n
    return sum

print(add(1,2,3,4))
print(add(1,2,3,4,5,6,7))
print(add(1,2,3,4,5,6,7,8,9,10))
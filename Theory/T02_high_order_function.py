def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 // n2

# In python this is called as a high order function
def cal(n1, n2, func):
    return func(n1 , n2)

# We can call any function through high order function
print(cal(2, 3, add))
print(cal(5, 3, sub))
print(cal(2, 3, mul))
print(cal(9, 3, div))
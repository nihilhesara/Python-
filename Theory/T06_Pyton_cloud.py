# https://www.pythonanywhere.com/
# day - 32

# day - 34 (Type hints)

def police_check(age:int) -> bool: # (variable name: data type) -> output data type IDE gives error when the type doesn't match
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check(12))
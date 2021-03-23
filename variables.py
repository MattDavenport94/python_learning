# A variable is a container for a value, which can be of various types

"""
This is a
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
"""

"""
VARIABLES RULES:
    - Variables names are case senistive (name and NAME are different varibles)
    - Must start with a letter or an underscore
    - Can have numbers but can not start with one
"""

# x = 1               # int
# y = 2.5             #float
# name = 'Matthew'    # str
# is_cool = True      # bool

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'Matthew', True)

# Basic math
a = x + y

# Casting 
x = str(x)
y = int(y)
z = float(y)

print(x, y, name, is_cool, a)
print(type(x))
print(type(y), y)
print(type(z), z)
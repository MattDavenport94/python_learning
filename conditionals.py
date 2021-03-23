# If/Else conditions are used to decide to do something based on something being true or false

x = 10
y = 50

a = 45
b = 45

c = 4
d = 9
# Comparison Operators(==, !=, >, <, =>, <=) - Used to compare values

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# If/else

if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')


# elif
if a > b:
    print(f'{a} is greater than {b}')
elif a == b:
    print(f'{a} is equal to {b}')
else:
    print(f'{b} is greater than {a}')

# Nested if statements
if c > 2:
    if c <= 10:
       print(f'{x} is greater than 2 and less than or equal 10') 


# Logical operators (and, or, not) - Used to combine conditional statements

# and
if d > 2 and d <= 10:
    print(f'{d} is greater than 2 and less than or equal 10')

# or
if d > 2 or d <= 10:
    print(f'{d} is greater than 2 and less than or equal 10')

# not
if not(c == d):
    print(f'{c} does not equal {d}')

# Membership Operators (not,  not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1,2,3,4,5]

# in
if c in numbers:
    print(c in numbers)

# not in
if c in numbers:
    print(c not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
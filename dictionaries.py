# A Dictionary is collection which is unordered, changeable and indexed. No duplicate members.

# Create a dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 26
}

# Use constructor
person2 = dict(first_name='Sarah', last_name='Williams', age=26)

print(person, type(person))
print(person2, type(person2))

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

# Remove item
del(person['age'])
person.pop('phone')

print(person)

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Matt', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people)

# Index multiple dict
print(people[1]['name'])
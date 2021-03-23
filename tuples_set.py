# A Tuple is a collection which is ordered and unchangedable. Allows duplicate members.

# Create tuples
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

# Single value needs trailing comma
fruits3 = ('Apples',)
print(fruits3, type(fruits3))

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

print(fruits2)

# Get the length of tuple
print(len(fruits2))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Remove from set
fruits_set.remove('Grape')

# Delete set
del fruits_set

# Clear set
fruits_set.clear()

# Add duplicate
fruits_set.add('Apples')
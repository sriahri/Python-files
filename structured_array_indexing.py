import numpy as np

Fruit = ('Grape', 'Apple', 'Banana')
Color = ('Purple', 'Red', 'Yellow')
Ranking = (3, 2, 1)

# Creating the structured array
q9 = np.zeros(3, dtype={'names': ('Fruit', 'Color', 'Ranking'),
                        'formats': ('U32', 'U16', 'i4')})

q9['Fruit'] = Fruit
q9['Color'] = Color
q9['Ranking'] = Ranking

# Print the array
print(q9)
print()
# Index for ['Purple', 'Red', 'Yellow']
q10 = q9['Color']
print(q10)
print()
# Index for ['Banana', 'Yellow', 1]
q11 = q9[2]
print(q11)
print()

# Index for Rankings less than 3
q12 = q9[q9['Ranking'] < 3]

print(q12)
print()

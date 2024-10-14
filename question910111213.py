# 9
lstudentname = ['Lara', 'Sean', 'Derek', 'Melanie', 'Andrew', 'Mathew']
# 9a
print(lstudentname)
# 9b
print(lstudentname[4])
# 9c
lstudentname.append('Talia')
print(lstudentname)
# 9d
lstudentname.pop(6)
# 9e
lstudentname.insert(0, 'Abhishek')
print(lstudentname)
# 9f
lstudentname.sort()
print(lstudentname)
# 9g
lstudentname.reverse()
# 9h
_lstudentname = ['Jalal', 'Chris', 'Daniel', 'Thomas', 'Raghavi']
# 9i
lstudentname.extend(_lstudentname)
print(lstudentname)

# 9j
lstudentname.clear()

# 10
ll = [6, 7, 8, 9, [1, 5, 6, 10]]
# 10a
print(ll[4])
# 10b
print(ll[4][2])

# 11
dgrade = {'Jalal': 9.7, 'Chris': 9.5, 'Daniel': 9.3, 'Thomas': 9.9, 'Raghavi': 10}
# 11a
print(dgrade['Thomas'])

# 12
dgrades = {'Jalal': [9.7, 9.5, 9.2], 'Chris': [9.5, 9.4, 9.9], 'Daniel': [9.3, 9.9, 9.7], 'Thomas': [9.9, 9.4, 9.8],
           'Raghavi': [10, 9.1, 9.6]}
# 12a
print(dgrades['Jalal'][1])

# 13
dlara = {'Lara': {'quiz': [10, 9, 8], 'exam': [100, 98, 97]}}
print(dlara)
# 13a
print(dlara['Lara']['exam'][0])

# 13b
dlara['Lara']['quiz'][2] = 10

# 13c
t = tuple([10, 9, 8])

# 13d
# We cannot update a tuple because it is immutable.

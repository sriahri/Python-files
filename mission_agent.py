# Input1 determining the number of soldiers jumped.
input1 = int(input())
# Input2 determines the positions of the soldiers
# The below statement is used to convert the given input into a 2-d array.
# If we already given the input 2-d array, then start working from line 10.
input2 = list(input().lstrip('{').rstrip('}').split('}'))
coords = [[input2[0][0], input2[0][2]]]
for i in input2[1:]:
    coords.append([i[2], i[4]])
d_x = set() # Set for unique values of x coordinates.
d_y = set() # Set for unique values of y coordinates.
# Calculation of number of building covered
for i in coords:
    d_x.add(i[0])
    d_y.add(i[1])
res = (len(d_x) + len(d_y)) * 8 - input1
print(res)
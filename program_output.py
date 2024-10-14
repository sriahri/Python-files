fun = ['rain', 'rain', 'go', 'away', 'come', 'again', 'another', 'day',
       'an', 'apple', 'a', 'day', 'keeps', 'the', 'doctor', 'away',
       'have', 'your', 'head', 'in', 'the', 'clouds']

part1 = fun[14::6]
part1.reverse()

for thing in part1:
    print(thing, end=' ')

part2 = fun[12]
print(part2, end=' ')

part3 = fun[-16:-26:-5]
part3 = part3[:int(len(part3)/2)]
for thing in part3:
    print(thing, end=' ')

part4 = fun[2::16]
part4 = part4[int(len(part4)/2):]
for thing in part4:
    print(thing, end=' ')

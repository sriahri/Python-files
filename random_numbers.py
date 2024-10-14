import random

file = open("file2.txt", 'w')
for i in range(1000):
    file.write(str(random.random()*10000//1))
    file.write('\n')

file.close()
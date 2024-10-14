import random
import datetime

file = open("file2.txt", 'w')
start_time = datetime.time()
for i in range(1000000):
    file.write(str(random.random()*10000//1))
    file.write('\n')

end_time = datetime.time()
print(end_time.second-start_time.second)
file.close()
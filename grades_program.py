from math import sqrt
def standard_deviation(lst):
    mean = sum(lst)/10
    x = 0
    for i in lst:
        x += (i-mean)**2
    std = sqrt(x/10)
    return std

f = open('grades.txt', 'r')
l = f.readlines()
assignments = []
mid = []
final = []
for i in l:
    s = i.split()
    assignments.append(int(s[0]))
    mid.append(int(s[1]))
    final.append(int(s[2]))
    
# Maximum grade in the final
print('The maximum grade in the final is {}'.format(max(final)))
# Number of students achieved a total score greater than 85%
count = 0
for i in range(10):
    total_marks = assignments[i] + mid[i] + final[i]
    if total_marks >= 85:
        count += 1
print('The number of students having toatl score of 85% and more is {}'.format(count))
# Mean and standard deviation of each assessment tool
mean = sum(assignments)/10
print('Mean of the assignment is {}'.format(mean))
std_assignment = standard_deviation(assignments)
print('The standard deviation of the assignment is {}'.format(std_assignment))
print('Mean of the mid terms is {}'.format(sum(mid)/10))
std_mid = standard_deviation(mid)
print('The standard deviation of the mids is {}'.format(std_mid))
print('Mean of the finals is {}'.format(sum(final)/10))
std_final = standard_deviation(final)
print('The standard deviation of the finals is {}'.format(std_final))
# Finding which assessment tools has maximum standard deviation
if std_assignment > std_mid and std_assignment > std_final:
    print('Standard deviation of assigment is maximum')
elif std_mid > std_assignment and std_mid > std_final:
    print('Standard deviation of mid is maximum')
else:
    print('Standard deviation of final is maximum')
# Number of students scored maximum marks in assignment.
count = 0
for i in assignments:
    if i == 20:
        count += 1
print('The number of students who scored maximum marks are {}'.format(count))
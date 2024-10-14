designation = input('Enter the designation:(Car, Truck, Senior citizen) ').title().upper()[0]
while designation not in ['C', 'S', 'T']:
    print('Please enter the valid designation from one of the three')
    designation = input('Enter the designation:(C, T, S) ').title().upper()[0]

start_time = input('Enter the start time in HH:MM ')
start_hour = int(start_time.split(':')[0])
start_minute = int(start_time.split(':')[1])
end_time = input('Enter the end time in HH:MM ')
end_hour = int(end_time.split(':')[0])
end_minute = int(end_time.split(':')[1])

while end_hour - start_hour < 0:
    print('Please enter valid start and end time: ')
    start_time = input('Enter the start time in HH:MM ')
    start_hour = int(start_time.split(':')[0])
    start_minute = int(start_time.split(':')[1])
    end_time = input('Enter the end time in HH:MM ')
    end_hour = int(end_time.split(':')[0])
    end_minute = int(end_time.split(':')[1])

difference = end_hour - start_hour
difference_minutes = end_minute - start_minute
if difference_minutes > 0:
    difference += 1
charge = 0
difference_hours = difference
if designation == 'C':
    difference -= 2
    if difference > 3:
        charge += 3 * 1
    else:
        charge += difference * 1
    difference -= 3
    charge += difference * 0.5

elif designation == 'T':
    difference -= 2
    if difference > 2:
        charge += 2 * 2
    else:
        charge += difference * 2
    difference -= 2
    charge += difference * 1

else:
    charge = 0

print('The ticket is as follows: ')
if designation == 'C':
    print('Designation: Car')
elif designation == 'T':
    print('Designation Truck')
else:
    print('Designation Senior Citizen')

print('The number of hours parked is {}'.format(difference_hours))
print('The charges is {}'.format(charge))

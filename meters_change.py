total_meters = int(input())

num_kilometers = total_meters // 1000
total_meters = total_meters % 1000
num_decameters = total_meters // 10
total_meters = total_meters % 10
num_meters = total_meters

print('Kilometers:', num_kilometers)
print('Decameters:', num_decameters)
print('Meters:', num_meters)

# List of elements from user
l = list(map(int, input().split()))
# Sort the elements based on their count
l.sort()
# sort the elements based on their count
# using the key attribute and the count method.
sorted_list = sorted(l, key = l.count, reverse=True)
print(sorted_list)
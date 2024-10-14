import numpy as np
np.random.seed(123)
my_arr = np.random.random_sample((10,))

print(my_arr)

try:
    start = int(input('enter the starting point of the sub array: '))
    end = int(input('enter the ending point of the sub array: '))
    assert start >= 0
    assert start < end
    assert end <= len(my_arr)
except:
    print('Please enter valid values!')

(remainder1, sub_arr, remainder2) = my_arr[:start], my_arr[start:end+1], my_arr[end+1:]
print(remainder1, sub_arr, remainder2)

sorted_arr = np.sort(sub_arr)
print('Sorted sub array is:')
print(sorted_arr)

result = np.concatenate((remainder1, sorted_arr, remainder2))
print('Result is: ')
print(result)

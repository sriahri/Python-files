def medianMatrix(matrix):
    numbers = [] # Store all the elements of the matrix in al list
    for i in matrix:
        for j in i:
            numbers.append(j)
    numbers.sort() # Sort the list
    length = len(numbers)
    # If the length is even, then median is average, else median is the middle element
    if length%2 == 0:
        median = (numbers[length//2] + numbers[length//2-1]) / 2
    else:
        median = numbers[length//2]
    return median

def meanMatrix(matrix):
    numbers = []
    for i in matrix:
        for j in i:
            numbers.append(j)
    mean = sum(numbers) / len(numbers) # sum oof numbers by length of numbers
    return mean

matrix = []
rows, cols = map(int, input("Enter the number of rows and number of columns separated by space: ").split())
print("Enter the matrix:")
for i in range(rows):
    matrix.append(list(map(int, input().split())))
print('The median is {}'.format(medianMatrix(matrix)))
print('The mean is {}'.format(meanMatrix(matrix)))
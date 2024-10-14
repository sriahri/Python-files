def function(n):
    integers = list(range(2, n+1)) # Generate a list of integers in the range.
    p = 2 # Set p value to 2
    while p < n: # Until p is greater than n
        for i in integers: # Traverse through the list.
            if i%p == 0: # If the current element is a multiple of p
                integers.remove(i) # Remove it from the list
        for i in integers: # Traverse through the list and find the element greater than the p.
            if i > p:
                p = i # If found, replace the value of p
                break
        else:
            p = n + 1 # Else, move of the loop.
    print(integers)

function(10)
function(100)
function(1000)
function(4521)
function(10000)
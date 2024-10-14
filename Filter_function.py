# Function to check whether a string is containing 
# greater or equal to than seven characters or not

def lengthGreaterThanSeven(s):
    if len(s) >= 7: # len is the inbuilt function to find length of a string.
        return True
    else:
        return False

these_names = ["ophelia", "alexander", "mitus", "prometheus", "carson"]

# filter function returns filter object.

filtered_values = filter(lengthGreaterThanSeven, these_names) 

# Printing the values after applying filter.

print(*filtered_values)
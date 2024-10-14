f = open("data.txt", "rb")

# sets Reference point to tenth
# position to the left from end
f.seek(-10, 2)

# prints current position
print(f.tell())

# Converting binary to string and
# printing
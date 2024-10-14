def ql_func(d, h, s):
    # Step 1: Check if values are valid
    if d <= 0 or h < 0 or s <= 0:
        return "Invalid"

    # Step 2: Calculate the estimated time using Naismith's Rule
    t = (d / s) + (h / 400)

    # Classify the walk based on the estimated time and climb
    if t < 4 and h < 200:
        return "Easy"
    elif t > 8 or h > 600:
        return "Hard"
    else:
        return "Medium"


# Test cases
print(ql_func(21, 600, 3.5))  # Output: "Medium"
print(ql_func(10, 150, 5))  # Output: "Easy"
print(ql_func(15, 800, 2))  # Output: "Hard"
print(ql_func(21, 265, 3))  # Output: "Medium"
print(ql_func(10, 187, 1))  # Output: "Hard"
print(ql_func(15, 931, 7))  # Output: "Hard"

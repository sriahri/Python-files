# # # n  =10
# # # counter = 0
# # # for i in range(0, n):
# # #     counter += 1
# # #
# # # print(counter)
# #
# #
# # x  =2
# # y = 3
# # y = y-1
# # x = x+y
# #
# # if y != 0:
# #     y = y-1
# #
# # print(x)
#
# def f(x):
#     if x <= 1:
#         return 0
#     elif x%2 == 0:
#         return f(x+1) + x
#     else:
#         return f(x-3) - x
#
# print(f(10))

# Recursive function to return gcd of a and b
def gcd(a, b):
    # Everything divides 0
    if (b == 0):
        return a
    return gcd(b, a % b)


# Driver program to test above function
a = 10
b = 2
if (gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print(0)

# This code is contributed by Danish Raza

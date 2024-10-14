memo = dict()
def comb(m, n):
    if m == 0 or n == 0:
        return 1
    if (m, n) not in memo:
        memo[(m, n)] = comb(m-1, n) + comb(m, n-1)
    return memo[(m, n)] 

def f(nums):
    if len(nums) <= 2:
        return 1
    root = nums[0]
    left = []
    right = []
    for n in nums[1:]:
        if n < root:
            left.append(n)
        if n > root:
            right.append(n)
    return comb(len(left), len(right)) * f(left) * f(right)

print( (f(nums)-1))
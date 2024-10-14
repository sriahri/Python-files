def maxSubArrayDivideAndConquer(nums):
    length = len(nums)
    # Assigning a minimum possible value to the maximum_sum value
    maximum_sum = -1 * max(nums) * max(nums)

    # We check for every sub array starting from i
    for i in range(length):
        sum_value = 0
        for j in range(i, length):
            sum_value = sum_value + nums[i]

            # If sum_value is greater than the maximum_sum, then update the maximum_sum
            maximum_sum = sum_value if sum_value > maximum_sum else maximum_sum

    return maximum_sum


def maxSubArray(a):
    length = len(a)
    # Assigning a minimum possible value to the maximum_sum value
    maximum_sum = -1 * max(a) * max(a)
    sum_value = 0

    for i in range(length):
        sum_value = sum_value + a[i]
        if sum_value > maximum_sum:
            maximum_sum = sum_value
        if sum_value < 0:
            sum_value = 0

    return maximum_sum


a = [6, -8, -4, -5, 67, 98, 17]
print(maxSubArray(a))

def maxSubArrayDivideAndConquer(nums):
    length = len(nums)
    # Assigning a minimum possible value to the maximum_sum value
    maximum_sum = -1 * max(nums) * max(nums)

    # We check for every sub array starting from i
    for i in range(length):
        sum_value = 0
        for j in range(i, length):
            sum_value = sum_value + nums[j]

            # If sum_value is greater than the maximum_sum, then update the maximum_sum

            maximum_sum = sum_value if sum_value > maximum_sum else maximum_sum
            # print(sum_value)
            # print(maximum_sum)

    return maximum_sum


def maxSubArrayKadane(nums):
    length = len(nums)
    # Assigning a minimum possible value to the maximum_sum value
    maximum_sum = -1 * max(nums) * max(nums) * max(nums)
    sum_value = 0

    for i in range(length):
        sum_value = sum_value + nums[i]

        maximum_sum = sum_value if sum_value > maximum_sum else maximum_sum

        sum_value = 0 if sum_value < 0 else sum_value

    return maximum_sum

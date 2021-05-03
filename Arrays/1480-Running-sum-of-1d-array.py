"""
nums: List[int]
return: List[int]
"""
# Brute force solution
def runningSum(nums):
    sum_array = []
    summation = 0
    for index, value in enumerate(nums):
        if index == 0:
            sum_array.append(value)
        else:
            for index2 in range(index + 1):
                summation += nums[index2]
            sum_array.append(summation)
            summation = 0
    return sum_array


test2 = [3, 1, 2, 10, 1]
# runningSum(test2)


def runningSumOptimized(nums):
    sum_array = []
    summation = 0
    for index, value in enumerate(nums):
        if index == 0:
            sum_array.append(value)
            summation += value
        else:
            summation += value
            sum_array.append(summation)
    return sum_array


runningSumOptimized(test2)
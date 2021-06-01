from typing import List

nums = [2, 5, 5, 11]
target = 10


def twoSum(nums: List[int], target: int) -> List[int]:
    arr_len = len(nums)

    for index, val in enumerate(nums):
        for index2 in range(index + 1, arr_len):
            if nums[index2] + val == target:
                return [index, index2]


print(twoSum(nums, target))


def two_sum_hash(nums: List[int], target: int) -> List[int]:
    already_seen = {}  # val : index

    for index, val in enumerate(nums):
        diff = target - val

        if diff in already_seen:
            return [already_seen[diff], index]
        else:
            already_seen[val] = index
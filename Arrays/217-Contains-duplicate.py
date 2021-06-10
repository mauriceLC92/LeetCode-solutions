from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    nums_set = set(nums)
    nums_len = len(nums)

    if len(nums_set) < nums_len:
        return True
    else:
        return False


def containsDuplicate(nums: List[int]) -> bool:
    numbers_seen = {}

    for value in nums:
        if value in numbers_seen:
            numbers_seen[value] = numbers_seen[value] + 1
            if numbers_seen[value] >= 2:
                return True
        else:
            numbers_seen[value] = 1
    return False

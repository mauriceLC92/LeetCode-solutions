    from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        seen_nums = {}
        
        for index, num in enumerate(nums):
            if num in seen_nums and abs(seen_nums[num] - index) <= k:
                return True
            else:
                seen_nums[num] = index

        return False


"""
Can also use the brute force solution of nested for loops.
Hits a time limit exceeded error on LeetCode for a big input
"""
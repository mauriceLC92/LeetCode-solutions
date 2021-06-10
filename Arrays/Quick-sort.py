from typing import List
from random import randint


def quick_sort(arr: List[int]):
    arr_len = len(arr)
    if arr_len < 2:
        return arr
    else:
        # should actually choose a random value for the pivot so the algorithm runs in best time on average.
        # One average choosing a random pivot will yield the fastest run time for this algorithm
        pivot = arr[0]
        less_than_pivot = [i for i in arr[1:] if i <= pivot]
        greater_than_pivot = [i for i in arr[1:] if i > pivot]

        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


test_arr = [10, 4, 5, 5, 2, 3]
print(quick_sort(test_arr))

# output = [2, 3, 4, 5, 5, 10]
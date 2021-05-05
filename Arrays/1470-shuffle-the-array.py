nums = [2, 5, 1, 3, 4, 7]

n = 3

nums_two = [1, 2, 3, 4, 4, 3, 2, 1]

n_two = 4

nums_three = [1, 1, 2, 2]

n_three = 2


def shuffle(nums, n):
    shuffled_array = []
    y_starting_index = n
    for index in range(len(nums)):
        shuffled_array.append(nums[index])
        shuffled_array.append(nums[y_starting_index])
        y_starting_index += 1
        if index == n - 1:
            print(shuffled_array)
            return shuffled_array


shuffle(nums, n)
shuffle(nums_two, n_two)
shuffle(nums_three, n_three)
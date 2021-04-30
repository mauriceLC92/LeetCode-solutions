def binary_search(inputArr, target):
    lowest_position = 0
    highest_position = len(inputArr) - 1

    while lowest_position <= highest_position:
        middle_position = lowest_position + (highest_position - lowest_position) // 2
        guess = inputArr[middle_position]

        if guess == target:
            return middle_position

        if guess > target:
            highest_position = middle_position - 1
        else:
            lowest_position = middle_position + 1

    return None


myOrderedList = [2, 5, 10, 17, 33, 36, 44, 99]
target = 17

print(binary_search(myOrderedList, target))

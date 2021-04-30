def find_smallest(arr):
    smallestIndex = 0
    smallestValue = arr[smallestIndex]

    index = 1

    while index < len(arr):
        if arr[index] < smallestValue:
            smallestValue = arr[index]
            smallestIndex = index

        index += 1

    return smallestIndex


def selection_sort(arr):
    sorted_array = []
    arr_len = len(arr)

    for i in range(arr_len):
        smallest_value_position = find_smallest(arr)
        sorted_array.append(arr.pop(smallest_value_position))

    print(sorted_array)
    return sorted_array


testArr = [5, 3, 6, 2, 10]

selection_sort(testArr)

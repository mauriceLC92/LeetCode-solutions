from typing import List


arr = [6, 10, 14, 20]
target = 12

arr.append(12)

maxArrIndex = len(arr) - 1

while maxArrIndex >= 0:
    if maxArrIndex == 0:
        break
    elif arr[maxArrIndex] < arr[maxArrIndex - 1]:
        current_value = arr[maxArrIndex]
        val_on_left = arr[maxArrIndex - 1]

        arr[maxArrIndex] = val_on_left
        arr[maxArrIndex - 1] = current_value

    elif arr[maxArrIndex] >= arr[maxArrIndex - 1]:
        break

    maxArrIndex -= 1

# print(arr)


my_string = "hello"

# Add spaces between each character in the string

string_with_spaces = ""
for letter in my_string:
    string_with_spaces += "{} ".format(letter)

# print(string_with_spaces)


static_array = ["one", "two", "three"]


def sum_items(arr: List[int]) -> int:
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        first_item_array = arr.pop(0)
        return first_item_array + sum_items(arr)


test_arr = [20, 20, 202, 20]
print("Sum of array", sum_items(test_arr))


def count_items(arr: List[int]) -> int:
    arr_len = len(arr)
    if arr_len == 1:
        return 1
    else:
        arr.pop(0)
        return 1 + count_items(arr)


test_arr = [20, 20, 202, 20]
print("Items in array", count_items(test_arr))


def maximum_number(arr: List[int]) -> int:
    pass
from typing import List


arr = [6, 10, 14, 20]
target = 12

arr.append(12)

maxArrIndex = len(arr) - 1

# while maxArrIndex >= 0:
# if maxArrIndex == 0:
#     break
# elif arr[maxArrIndex] < arr[maxArrIndex - 1]:
#     current_value = arr[maxArrIndex]
#     val_on_left = arr[maxArrIndex - 1]

#     arr[maxArrIndex] = val_on_left
#     arr[maxArrIndex - 1] = current_value

# elif arr[maxArrIndex] >= arr[maxArrIndex - 1]:
#     break

# maxArrIndex -= 1

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


test_arr = [20, 20, 202, 20, 100, 456, 7]
print("Items in array", count_items(test_arr))


def maximum_number(arr: List[int]) -> int:
    arr_len = len(arr)
    if arr_len == 1:
        return arr[0]
    else:
        highest_value = arr[0]
        last_value = arr.pop()
        if last_value > highest_value:
            arr[0] = last_value
        return maximum_number(arr)


test_arr = [20, 20, 202, 20, 100, 456, 7]
print("Highest value in array", maximum_number(test_arr))


def quick_sort(arr):
    arr_len = len(arr)

    if arr_len < 2:
        return arr
    else:
        # The pivot should be a random value to achieve the average case which is the best case
        pivot = arr[0]
        # Now we partition into a side less than the pivot vale and a side greater than the pivot value

        less_than = [i for i in arr if i <= pivot]
        greater_than = [i for i in arr if i > pivot]

        return quick_sort(greater_than) + [pivot] + [less_than]


my_set = {1, 2, 3, 4, 5, 7, 9}

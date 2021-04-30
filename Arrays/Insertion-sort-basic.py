def insertion_sort(arr, target):
    arr.append(target)

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


arr = [6, 10, 14, 20]
target = 12

print("Before", arr)
insertion_sort(arr, target)
print("After", arr)

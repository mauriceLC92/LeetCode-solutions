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

print(arr)


my_string = "hello"

# Add spaces between each character in the string

string_with_spaces = ""
for letter in my_string:
    string_with_spaces += "{} ".format(letter)

print(string_with_spaces)


static_array = ["one", "two", "three"]

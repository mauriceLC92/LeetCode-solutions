def duplicate_zeros(input: list):
    amount_of_zeros = input.count(0)
    array_length = len(input)

    for num in range(array_length - 1, -1, -1):
        if num + amount_of_zeros < array_length:
            input[num + amount_of_zeros] = input[num]
        if input[num] == 0:
            amount_of_zeros -= 1
            if num + amount_of_zeros < array_length:
                input[num] = 0
    return input


# Need to finish the Python solution

duplicate_zeros([1, 5, 2, 0, 6, 8, 0, 6, 0])

print(duplicate_zeros([1, 5, 2, 0, 6, 8, 0, 6, 0]))

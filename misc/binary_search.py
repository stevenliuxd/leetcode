def binary_search(arr, target):
    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer <= right_pointer:
        middle_pointer = int((left_pointer + right_pointer)/2)
        if target < arr[middle_pointer]:
            right_pointer = middle_pointer - 1
        elif target > arr[middle_pointer]:
            left_pointer = middle_pointer + 1
        else:
            return middle_pointer
    return -1

arr = [2, 3, 10, 200, 15, 16, 47, 29, 92, 82, 73, 210, 666, 1, 3, 4, 1, -2, -68]

arr.sort()
print("Input target: ")
target = int(input()) # User inputs target value, assume within arr, but return error if DNE in array

print("Begin calculation...")
print(binary_search(arr, target))
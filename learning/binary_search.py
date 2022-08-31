def binary_search(arr, target):
    left_pointer = 0
    right_pointer = len(arr) - 1
    loop_count = 0

    while left_pointer <= right_pointer:
        loop_count += 1
        middle_pointer = int((left_pointer + right_pointer)/2)
        if target == arr[middle_pointer]:
            print("Loop count: " + str(loop_count))
            return middle_pointer # The answer
        elif target > arr[middle_pointer]:
            left_pointer = middle_pointer
        else:
            right_pointer = middle_pointer
    
    return -1

arr = [2, 3, 10, 200, 15, 16, 47, 29, 92, 82, 73, 210, 666, 1, 3, 4, 1, -2, -68]

arr.sort()
print("Input target: ")
target = int(input()) # User inputs target value, assume within arr, but return error if DNE in array

print("Begin calculation...")
print(binary_search(arr, target))
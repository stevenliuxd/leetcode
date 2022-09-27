import random

arr = []

for i in range(10000):
    arr.append(random.randint(1, 2000))

def quicksort(arr):
    qs(arr, 0, len(arr) - 1)

def qs(arr, l, r):
    if l >= r: # Section of array has 1 or fewer elements; skip
        return
    p = partition(arr, l, r)

    qs(arr, l, p - 1)
    qs(arr, p + 1, r)

def partition(arr, l, r):
    pivot = arr[r] # Pick pivot as value of last index in array
    i = l - 1 # start pointer i at 0
    for j in range(l, r): # loop pointer j from the beginning to the last index in array
        if arr[j] < pivot: # if at any point the current value is less than the pivot, increase pointer i by one and SWAP values between i and j
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1] # finally, swap the pivot such that it is in the middle of the array
    return i + 1

print('Begin')
quicksort(arr)
print('End')
print(arr)

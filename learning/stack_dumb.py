def stack(string, i, j, arr, l, r):
    if string[i] == l:
        j += 1
        arr[j] = l
    elif string[i] == r:
        if j >= 0 and arr[j] == l:
            arr[j] = None
            j -= 1
        else:
            j += 1
            arr[j] = r
    return [j, arr]

def isBalanced(string):
    arr = [None] * len(string)
    j = -1
    for i in range(0, len(string)): # Time Complexity is O(n) where n is the number of elements in the string
        [j, arr] = stack(string, i, j, arr, "(", ")")
        [j, arr] = stack(string, i, j, arr, "[", "]")
        [j, arr] = stack(string, i, j, arr, "{", "}")
    if j == -1:
        return True
    else:
        return False

string = "([])(){}(())()()"
print(isBalanced(string))
string1 = "()[]{)"
print(isBalanced(string1))



from collections import deque

def isBalanced(string):

    stack = deque()
    hashmap = {
        "{" : "}",
        "[" : "]",
        "(" : ")",
    }

    for i in string:
        if i in hashmap:
            stack.append(i)
        elif i in hashmap.values():
            other_pair = (list(hashmap.keys())[list(hashmap.values()).index(i)])
            if len(stack) > 0 and stack[-1] == other_pair:
                stack.pop()
            else:
                return False
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

str1 = "())"
str2 = "([])(){()}(())()()"
print(isBalanced(str1))
print(isBalanced(str2))

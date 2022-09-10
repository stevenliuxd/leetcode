def helper(root, min_value, max_value):
    if not root:
        return True
    if root.val < min_value or root.val > max_value:
        return False
    return helper(root.left, min_value, root.val-1) and helper(root.right, root.val+1, max_value)

def isBinSearchTree(root):
    ranges = [0, 10000]
    return helper(root, ranges[0], ranges[1])
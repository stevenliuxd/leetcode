class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

l1 = TreeNode(2)
l2l = TreeNode(3)
l2r = TreeNode(4)
l3l = TreeNode(5)
l3r = TreeNode(6)
l1.left = l2l
l1.right = l2r
l2l.left = l3l
l2l.right = l3r


def findSum(root):
    if root is None:
        return 0
    else:
        return root.val + findSum(root.left) + findSum(root.right)

def getHeight(root):
    if root is None:
        return -1
    return 1 + max(getHeight(root.left), getHeight(root.right))

def getDepth(root):
    if root is None:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))

def getmaxDiameter(root):

    a = [0]
    def dfs(root):
        if root is None:
            return -1
        left = getHeight(root.left)
        right = getHeight(root.right)
        a[0] = max(a[0], 2 + left + right)
        return 1 + max(left, right)
    dfs(root)
    return a[0]

def dfs(root, list1):
    if not root:
        return
    
    dfs(root.left, list1)
    dfs(root.right, list1)

    list1.append(root.val)
    return
    
def helper(root, min_value, max_value):
    if not root:
        return True
    if root.val < min_value or root.val > max_value:
        return False
    return helper(root.left, min_value, root.val-1) and helper(root.right, root.val+1, max_value)

def isBinSearchTree(root):
    ranges = [0, 10000]
    return helper(root, ranges[0], ranges[1])

#print(findSum(l1))
#print(getHeight(l1))
#print(getmaxDiameter(l1))
print(isBinSearchTree(l1))


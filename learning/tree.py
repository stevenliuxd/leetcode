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
    
print(findSum(l1))
print(getHeight(l1))
print(getmaxDiameter(l1))

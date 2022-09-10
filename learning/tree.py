class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def insertleft(self, val):
        if not self.left:
            self.left = TreeNode(val)
        else:
            temp = self.left
            self.left = TreeNode(val)
            self.left.left = temp

l1 = TreeNode(5)
l2l = TreeNode(10)
l2r = TreeNode(15)
l3l1 = TreeNode(20)
l3l2 = TreeNode(25)
l3r1 = TreeNode(30)
l3r2 = TreeNode(35)
l4l = TreeNode(45)
test = l1
l1.left = l2l
l1.right = l2r
l2l.left = l3l1
l2l.right = l3l2
l2r.left = l3r1
l2r.right = l3r2
l3l2.right = l4l


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
        left = dfs(root.left)
        right = dfs(root.right)
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

    return list1
    
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
#print(getHeight(l3l2))
#print(getDepth(l1))
#print(test.right.val)
#print(getmaxDiameter(l1))
list1 = []
print(dfs(l1, list1))
#print(isBinSearchTree(l1))



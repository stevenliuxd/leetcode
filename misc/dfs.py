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

def getDepth(root, x):
    if not root:
        return -1
    dist = -1
    if root.val == x:
        return dist + 1
    dist = getDepth(root.left, x)
    if dist >= 0:
        return dist + 1
    dist = getDepth(root.right, x)
    if dist >= 0:
        return dist + 1
    return dist
print(getDepth(l1, 25))

height = [0]
def getHeight(root, x):
    if not root:
        return -1
    left = getHeight(root.left, x)
    right = getHeight(root.right, x)
    if root.val == x:
        height[0] = 1 + max(left, right)
    return 1 + max(left, right)
#getHeight(l1, 5)
#print(height[0])

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
    return root.val

#list1 = []
#print(dfs(l1, list1))
#print(list1)




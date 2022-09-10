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
l1.left = l2l
l1.right = l2r
l2l.left = l3l1
l2l.right = l3l2
l2r.left = l3r1
l2r.right = l3r2
l3l2.right = l4l

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [root.val]
        
        def dfs(root):
            
            # Base case
            if not root:
                return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            
            # Calculate case for both sides split
            res[0] = max(res[0], root.val + left + right)
            # Calculate case for one side split, return ans
            
            ans = root.val + max(left, right)
            return ans
        dfs(root)
        return res[0] 
print(Solution().maxPathSum(l1))
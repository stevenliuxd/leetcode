# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque() # Instantiate queue 
        result = [] # Create results list to store nodes
        
        if root: # If root node exists then append it, otherwise it'll just return []
            queue.append(root)
        
        while queue: # while queue is not empty
            level = [] # Create list to append all nodes in the current "level"
            for i in range(len(queue)): # Loop through every node on that level. First level has only root node
                vertex = queue.popleft() # Retrieve the first node inserted 
                level.append(vertex.val) # Add this node to the current level
                
                # If there is a left/right node, add it to the queue. It'll only get popped after everything from
                # the current level gets popped
                if vertex.left: 
                    queue.append(vertex.left)
                if vertex.right:
                    queue.append(vertex.right)
            result.append(level) # Append all nodes found on this level into the master result 
                    
        
        return result
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

l1 = Tree(2)
l2l = Tree(3)
l2r = Tree(4)
l3l = Tree(5)
l3r = Tree(6)
l1.left = l2l
l1.right = l2r
l2l.left = l3l
l2l.right = l3r


def find_sum(root):

    if root == None:
        return 0
    else:
        return root.data + find_sum(root.left) + find_sum(root.right)

    
print(find_sum(l1))

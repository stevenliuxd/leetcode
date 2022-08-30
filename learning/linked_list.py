class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

nodeB.prev = nodeA
nodeC.prev = nodeB
nodeD.prev = nodeC
nodeE.prev = nodeD

def countNodes(head):
    count = 0
    current_node = head

    while current_node.next != None:
        current_node = current_node.next
        count+=1
    
    return count

ans = countNodes(nodeA)
print(ans)

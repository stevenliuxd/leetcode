class Node:
    def __init__(self, val):
        self.val = val
        self.edge = []

    def add_edge(self, edge):
        self.edge.append(edge)
    
    def traverse(self):
        traversed = []
        queue = []
        for ed in self.edge: # Append current edges into the queue
            queue.append(ed)
        while len(queue) != 0: # While queue is not empty
            vertex = queue.pop() # Pop the vertex and check if it is traversed
            if vertex not in traversed: 
                print(vertex.data) 
                traversed.append(vertex) # Add vertex into traversed list 
                for ed in vertex.edge:
                    queue.append(ed)
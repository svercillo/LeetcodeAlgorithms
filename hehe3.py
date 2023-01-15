
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid) -> 'Node':
        n = len(grid)
        
        def create_node(tl, length):
            if length == 1:
                return Node(grid[tl[0]][tl[1]], True, None, None, None, None) # base case

            values = []
            node = Node(-1, False, None, None, None, None)
            for i in range(2):
                for j in range(2):
                    next_tl = tl.copy()
                    if i == 0:
                        next_tl[0] += length // 2
                    if j == 0:
                        next_tl[1] += length // 2
                    
                    next_node = create_node(next_tl, length // 2)
                    
                    if next_node.isLeaf:
                        values.append(next_node)
                    
                    match (i,j):
                        case (0,0):
                            node.topLeft = next_node
                        case (0,1):
                            node.topRight = next_node
                        case (1,0):
                            node.bottomLeft = next_node
                        case (1,1):
                            node.bottomRight = next_node

                    
            
            # values.sort(key = lambda k : k.val)
            # if len(values) == 4 and values[0] == values[-1]:
            #     node.isLeaf = True
            #     node.val = values[0]
            #     node.topLeft = None
            #     node.topRight = None
            #     node.bottomLeft = None
            #     node.bottomRight = None

            return node
            

        return create_node([0,0], n)



        

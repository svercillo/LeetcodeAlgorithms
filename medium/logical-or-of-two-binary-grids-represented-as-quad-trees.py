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
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        node = quadTree1


        def create_node(node1, node2): # continue until one is a leaf and one is not
            if node1.isLeaf and node2.isLeaf: 
                val = 0             
                if node1.val == 1 or node2.val == 1:
                    val = 1
                return Node(val, True, None, None, None, None)
            else: 
                if (node1.isLeaf and node1.val == 1) or (node2.isLeaf and node2.val == 1): 
                    return Node(1, True, None, None, None, None)
                
                # this node is going to not be a leaf
                if node1.isLeaf and not node2.isLeaf:
                    nodetl = create_node(node1, node2.topLeft)
                    nodetr = create_node(node1, node2.topRight)
                    nodebl = create_node(node1, node2.bottomLeft)
                    nodebr = create_node(node1, node2.bottomRight)
                elif not node1.isLeaf and node2.isLeaf:
                    nodetl = create_node(node1.topLeft, node2)
                    nodetr = create_node(node1.topRight, node2)
                    nodebl = create_node(node1.bottomLeft, node2)
                    nodebr = create_node(node1.bottomRight, node2)
                else:
                    nodetl = create_node(node1.topLeft, node2.topLeft)
                    nodetr = create_node(node1.topRight, node2.topRight)
                    nodebl = create_node(node1.bottomLeft, node2.bottomLeft)
                    nodebr = create_node(node1.bottomRight, node2.bottomRight)

                if (
                    (nodetl.isLeaf and nodetr.isLeaf and nodebl.isLeaf and nodebr.isLeaf)
                    and (nodetl.val == 1 and nodetr.val == 1 and nodebl.val == 1 and nodebr.val == 1)
                ): 
                    return Node(nodetl.val, True, None, None, None, None)

                return Node(-1, False, nodetl, nodetr, nodebl, nodebr)

        return create_node(quadTree1, quadTree2)
            

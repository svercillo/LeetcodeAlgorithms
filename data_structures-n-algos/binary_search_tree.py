''' Implementation of BinarySearchTree:
Stores every added element in a balanced binary tree
'''

class BinarySearchTree:
    class Node: 
        def __init__(self, value, left, right, parent):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

        node1 = self.Node(1, )
    
    def _add_node(self, node: Node):
        if self.root is not None:
            self.root = node 
            node.left = None
            node.right = None



    


        
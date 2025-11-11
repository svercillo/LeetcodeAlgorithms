"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root
        
        nodes =[] 
        def dfs(node):

            if not node:
                return

            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
            
        dfs(root)

        n = len(nodes)
        for i in range(n -1): 

            a = nodes[i]
            b = nodes[i+1]

            a.right = b
            b.left = a



        nodes[0].left = nodes[-1]
        nodes[-1].right = nodes[0]


        return nodes[0]



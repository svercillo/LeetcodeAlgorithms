"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""



class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = [(root, 0)] 
        if root is None: return []
        
        res = []
        while len(queue) > 0: 
            front_node, level = queue.pop()

            if level >= len(res):
                res.append([front_node.val])
            else: 
                res[len(res) -1].append(front_node.val)
            
            
            for child in front_node.children:
                queue.insert(0, (child, level+1))

                
            
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_nodes = [0]
        
        def recurse(node, m_val):
            if node is None: 
                return
            
            if node.val >= m_val:
                # print(node.val, m_val)
                num_nodes[0] += 1
            
                m_val = node.val
            
            recurse(node.left, m_val)
            recurse(node.right, m_val)
        
        recurse(root, -math.inf)
        
        return num_nodes[0]

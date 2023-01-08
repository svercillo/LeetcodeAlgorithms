# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        contains = set()
        
        def dfsR2(node):
            nonlocal contains
            
            if not node:
                return
            
            
            contains.add(node.val)
            
            dfsR2(node.right)
            dfsR2(node.left)
            
        
        dfsR2(root2)
        
        def dfsR1(node):
            nonlocal contains, target
            
            
            if not node:
                return False
            
            if target - node.val in contains:
                return True
        
            
            val = dfsR1(node.left) or dfsR1(node.right)
              
            return val
        
        return dfsR1(root1)
            
            
        
        
        
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        diameter = 0 
        
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            
            
            
            lsum = dfs(node.left)
            rsum = dfs(node.right)
            
            diameter = max(lsum + rsum, diameter)
            
            
            return max(lsum, rsum) +1
        
        dfs(root)
        
        return diameter
            

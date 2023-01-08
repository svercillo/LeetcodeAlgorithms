# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.s = 0
        if root is None:
            return 0
        
        
        def dfs(node, left):
            global s
            
            if not node: 
                return
            
            
            if not node.left and not node.right and left:
                self.s += node.val
                
            dfs(node.left, True)
            dfs(node.right, False)

        
        dfs(root, False)
        
        return self.s
        
        
        

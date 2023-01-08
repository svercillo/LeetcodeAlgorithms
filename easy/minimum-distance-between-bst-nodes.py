# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.prev = -math.inf
        
        self.res = math.inf
        def dfs(node):
            global res
            global prev
            
            if not node: 
                return
            
            dfs(node.left)
            
            self.res = min(self.res, node.val - self.prev)
            self.prev = node.val
            
            dfs(node.right)
            
            
        dfs(root)
        
        return self.res
            

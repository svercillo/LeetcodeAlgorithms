# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        
        self.invalid = False
        self.dfs(root, 0)
    
        return not self.invalid
    
    
    def dfs (self, node, height): # return the max height at node
        # print(node, height)
        if self.invalid or (not node.left and not node.right) :
            return height
        
        if node.left and node.right:
            l_height = self.dfs(node.left, height +1)
            r_height = self.dfs(node.right, height +1)
        
        elif not node.left and node.right:
            l_height = height
            r_height = self.dfs(node.right, height +1)
        elif not node.right and node.left:
            r_height = height
            l_height = self.dfs(node.left, height +1)
        
        
        if abs(l_height - r_height) > 1:
            self.invalid = True

        return max(l_height, r_height)

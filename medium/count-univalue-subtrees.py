# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            return 0
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return True
            
            if not node.left and not node.right: 
                count += 1
                return True
            
        
            lvalid = dfs(node.left)
            rvalid = dfs(node.right)
            
            if not lvalid or not rvalid:
                return False
            
            if node.left: 
                if node.right:
                    if node.val == node.right.val == node.left.val:
                        count += 1 
                        return True
                elif node.val == node.left.val:
                    count += 1 
                    return True
                        
                
            elif node.right:
                if node.val == node.right.val:
                    count += 1
                    return True
            
            return False
    
        dfs(root)
        return count

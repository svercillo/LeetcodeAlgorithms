# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        self.res = True
        
        prev = []
        def dfs(node, level):
            
            if not node: 
                return
            
            if level +1 > len(prev):
                prev.append(None)
                
            if prev[level]:
                if level % 2 == 0: 
                    if node.val <= prev[level]:
                        self.res = False
                        return
                else:
                    if node.val >= prev[level]:
                        self.res = False
                        return
                    
            prev[level] = node.val
            
            if ((level %2 + node.val %2) %2 != 1):
                self.res = False
                return 
                
        
            
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            
            
        
        dfs(root, 0)
        
        
        return self.res

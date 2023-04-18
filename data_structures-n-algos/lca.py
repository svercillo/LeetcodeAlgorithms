# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p: int,  q: int):
        
        lca = None
        
        def dfs(node):
            nonlocal p, q, lca
            
            if not node or lca is not None:
                return False, False

            containsp = False
            containsq = False
            
            
            res1 = dfs(node.left)
            res2 = dfs(node.right)
            
            containsp = containsp or res1[0] or res2[0]
            containsq = containsq or res1[1] or res2[1]
            

            if node.val == p:
                containsp = True
            elif node.val == q: 
                containsq = True
                
            # print(node.val, containsp, containsq)
            
            if containsp and containsq and not lca: 
                lca = node    
            
            return containsp, containsq
        
        dfs(root)

        return lca

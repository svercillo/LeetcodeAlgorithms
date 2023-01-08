# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:        
        '''
        three cases:
            q child of p
            p child of q
            neither child of the other
        ''' 
        
        
        if p == q:
            return 0
        containsp = set()
        containsq = set()
        lca = None
        
        def dfs(node):
            nonlocal p, q, lca
            
            if not node:
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
        # print(lca.val)
        
        
        
        def findDist(node, targ, dist):
            if not node:
                return 0
            
            if node.val == targ:
                return dist
            
            
            res1 = findDist(node.left, targ, dist +1)
            res2 = findDist(node.right, targ, dist +1)
            
            return sum([res1, res2])
        
        res1 = findDist(lca, p, 0)
        res2 = findDist(lca,q, 0)
        
        return sum([res1, res2])

            
            
        
        
        
        

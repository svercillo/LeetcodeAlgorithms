# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        lca = [None]
        
        
        def recurse(node, p, q):
            
            if not node:
                return 0
            
            val = 0
            if node.val  == p.val: 
                val +=1 
                
            if node.val  == q.val: 
                val +=1 
            
            val += recurse(node.left, p, q)
            val += recurse(node.right, p, q)
            
            if val >= 2 and lca[0] is None:
                if node is not None:
                    lca[0] = node
                
            return val
        
            
    
        recurse(root, p, q)
        
        
        return lca[0]

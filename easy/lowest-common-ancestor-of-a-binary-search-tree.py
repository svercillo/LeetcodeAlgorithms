# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        
        if root.val == p.val == q.val: 
            return root
        
        lca = [None]
        
        
        def recurse(node, p, q):
            
            if not node: return
            
            if p.val == node.val or q.val == node.val:
                lca[0] = node
                return
            
            
            if p.val < node.val :
                if q.val > node.val:
                    lca[0] = node
                    return 
            elif p.val > node.val:
                if q.val < node.val: 
                    lca[0] = node
                    return
            
            recurse(node.left, p, q)
            recurse(node.right, p, q)
        
    
        recurse(root, p, q)
        
        
        return lca[0]

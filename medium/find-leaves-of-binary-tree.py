# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        parents = {}
        child = {} 
        
        res = []        
        leaves = []
        def dfs(node, parent):
            nonlocal parents, child
            
            if not node:
                return
                
            num_child = 0
            if node.left:
                num_child += 1
            if node.right:
                num_child += 1
            
            child[id(node)] = num_child
        
            if parent:
                parents[id(node)] = parent
            
            if not node.left and not node.right:
                leaves.append(node)
            
            dfs(node.left, node )
            dfs(node.right, node)
            
                    
        dfs(root, None)
        
        while len(leaves) > 0:
            new_leaves = []
            int_res = []
            for l in leaves:
                int_res.append(l.val)
                
                if len(new_leaves) > 0 and id(new_leaves[-1]) == id(parents[id(l)]):
                    continue
                    
                
                if id(l) in parents:
                    par = parents[id(l)]
                    child[id(par)] -= 1

                    if child[id(par)] == 0:        
                        new_leaves.append(par)
                    
            leaves = new_leaves
            res.append(int_res)
                
        return res

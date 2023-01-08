class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        res = [] 
        def dfs(node):
            if node is None:
                return
            res.append(node.val)
            
            for child in node.children:
                dfs(child)
            
            
        dfs(root)
        return res

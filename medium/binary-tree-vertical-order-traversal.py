# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        min_col = 0
        max_col = 0 
        col_map = {}
        
        if not root: 
            return []
        
        def dfs(node, col, height):
            
            nonlocal min_col
            nonlocal max_col
            if not node:
                return
            
            # print(node.val)

            if col not in col_map:
                if col < min_col:
                    min_col = col
                elif col > max_col:
                    max_col = col 
                col_map[col] = []
            
            col_map[col].append((node.val, height))
            
            dfs(node.left, col - 1, height +1)
            dfs(node.right, col + 1, height + 1)
        
        dfs(root, 0, 0)
        
        res = []
        for i in range(min_col, max_col +1):
            col_map[i].sort(key=lambda k : k[1]) # sort on height
            res.append([tup[0] for tup in col_map[i]])
        return res
        
            

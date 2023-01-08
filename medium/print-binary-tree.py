# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        depth = self.maxDepth(root)
        
        results = []
        for i in range(depth):
            num_base_leaves = 2 **(depth)
            # print(num_base_leaves)
            arr = [""] * (num_base_leaves - 1)
            
            results.append(arr)
        
        
        
        def dfs(node, i, j):
            
            if node is None: return
            
            results[i][j] = str(node.val)
            
            dfs(node.left, i + 1, j - 2 ** (depth -2 - i))
            dfs(node.right, i + 1 , j + 2 ** (depth -2 -i ))
            
            
        
        dfs(root, 0, len(results[0]) //2)
        
        return results
            
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        
        m = {}
        def dfs(node):
            nonlocal m
            if not node:
                return 0
                    
            lsum = dfs(node.left)
            rsum = dfs(node.right)
        
            _sum = lsum + rsum + node.val
            if _sum not in m: 
                m[_sum] = id(node) 
            return _sum
        
        total = dfs(root)
        if total  % 2 == 1:
            return False
        
        
        # print(m, id(root))
        return total // 2 in m and m[total // 2] != id(root) 

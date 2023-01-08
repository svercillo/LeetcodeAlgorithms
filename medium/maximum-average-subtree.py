# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        # res = [num, average, max_average]
        def dfs(node):
            
            if not node:
                return 0, 0, 0
                
                
            
            n1, a1, ma1 = dfs(node.left)
            n2, a2, ma2 = dfs(node.right)
            
            
            num = n1 + n2 + 1 
            average = sum([n1*a1, n2 * a2, 1* node.val]) / num
            
            return num, average, max(average, ma1, ma2)
            
            
        return dfs(root)[2]

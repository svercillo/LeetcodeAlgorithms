# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            
            if not node:
                return 0,0
            
            takeScoreL, leaveScoreL = dfs(node.left)
            takeScoreR, leaveScoreR = dfs(node.right)
                    
            takeScore = node.val + leaveScoreL + leaveScoreR
            leaveScore = max([
                leaveScoreL + leaveScoreR,
                leaveScoreL + takeScoreR,
                takeScoreL + leaveScoreR,
                takeScoreL + takeScoreR
            ])
            
            # print(node.val, takeScore, leaveScore)
                            
            return takeScore, leaveScore
            
            
        return max(dfs(root))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        res = defaultdict(int )
        
        @cache
        def longestpath(node):
            value = node.val
            # print("processing", node, value)
            path = 1
            if node.left and node.left.val == value: 
                path = max(path, longestpath(node.left) + 1)

            if node.right and node.right.val == value: 
                path = max(path, longestpath(node.right) + 1)
            
            return path


        def dfs(node):
            if not node:
                return node
            
            res[node.val] = max(res[node.val], longestpath(node))

            if node.left and node.right and node.left.val == node.val and node.right.val == node.val:
                res[node.val] = max(res[node.val], longestpath(node.left) + longestpath(node.right) + 1)
            

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return max(list(res.values())) -1

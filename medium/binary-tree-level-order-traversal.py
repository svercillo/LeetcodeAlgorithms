# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = [root]
        while len(q):
            # print([node.val for node in q if node])
            row = []
            
            row_result = [node.val for node in q if node]
            if len(row_result):
                res.append(row_result)
            
            for node in q:
                if node:
                    row.append(node.left)
                    row.append(node.right)

            q = row
            
            
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        q = [root]

        res = []
        depth = 0
        while len(q):
            new_q = []
            res_row = []

            
            for node in q:
                if not node:
                    continue 
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)

            
            if depth % 2 == 1:
                q = reversed(q)

            for node in q:
                if not node: continue
                res_row.append(node.val)

            if len(res_row):
                res.append(res_row)
                
            depth += 1 
            q = new_q

        return res

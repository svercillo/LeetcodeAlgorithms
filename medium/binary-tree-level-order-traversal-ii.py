# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = deque()
        if not root:
            return []

        q = [root]
        while len(q):
            new_q = []
            row = []

            for node in q:
                row.append(node.val)
                if node.left:
                    new_q.append(node.left)
                
                if node.right: 
                    new_q.append(node.right)

            res.appendleft(row)
            q = new_q

        return [arr for arr in res]
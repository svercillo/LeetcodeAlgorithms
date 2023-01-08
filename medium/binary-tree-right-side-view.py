# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if not root: 
            return []
        queue = deque([(root, 0)])
        
        while len(queue) >0:
            print(queue)
            node, level = queue.popleft()
                
            if len(queue) == 0 or queue[0][1] > level:
                res.append(node.val)

            if node.left:
                queue.append((node.left, level +1))

            if node.right:
                queue.append((node.right, level +1))
        
        
        return res
    

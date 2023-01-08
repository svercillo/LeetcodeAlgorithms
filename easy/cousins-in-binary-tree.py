# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        if x == root.val or y == root.val:
            return False
        q = [(root, None)]
        while len(q):
            new_q = []

            
            found = [] 
            for node, parent in q:
                if node:
                    if node.val == x or node.val == y:
                        found.append(parent.val)
                    new_q.append((node.left, node))
                    new_q.append((node.right, node))


            print(found)
            if len(found) == 1:
                return False
            elif len(found) == 2: 
                return found[0] != found[1]
            q = new_q
        
        return False
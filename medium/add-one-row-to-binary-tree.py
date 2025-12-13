# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1: 
            return TreeNode(val, root)

        q = [root]
        depth -= 1

        while depth > 1:            
            nq = []                
            
            for node in q: 
                if not node:
                    continue
                nq.append(node.left)
                nq.append(node.right)

            q = nq
            depth -= 1


        for node in q:
            if not node:
                continue

            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)

        

        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        prehead = TreeNode(1, None, root)



        def contains_one(node):
            if not node:
                return False

            left_contains = contains_one(node.left)
            right_contains = contains_one(node.right)

            if not left_contains:
                node.left = None
            
            if not right_contains:
                node.right = None 

            if not left_contains and not right_contains and node.val == 0:
                return False
            
            return True


        contains_one(prehead)

        return prehead.right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        

        if not root:
            return 

        def removeleaves(node):
            if node.left and removeleaves(node.left):
                    node.left = None
            if node.right and removeleaves(node.right):
                node.right = None

            if not node.left and not node.right and node.val == target:
                return True

        if removeleaves(root):
            return None

        return root



                

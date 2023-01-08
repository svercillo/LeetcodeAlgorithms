# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        
        closest = math.inf
        node = root
        while node is not None:
            if abs(target - node.val) < abs(target - closest):
                closest = node.val
            if target > node.val:
                node = node.right
            else:
                node = node.left
            
        return closest

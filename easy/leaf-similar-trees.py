# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        arr1 = []
        arr2 = []
        self.recurse(root1, arr1)
        self.recurse(root2, arr2)
        
        return arr1 == arr2 
        
    def recurse(self, root, arr):
        if root is None:
            return
        
        self.recurse(root.left, arr)
        self.recurse(root.right, arr)
        if root.right is None and root.left is None:
            arr.append(root.val)
        

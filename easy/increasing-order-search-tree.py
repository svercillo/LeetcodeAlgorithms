# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.recurse(root, arr)
        
        for i in range(len(arr)-1):
            arr[i].left = None
            arr[i].right = arr[i+1]
        
        arr[len(arr) -1].left = None
        arr[len(arr) -1].right = None 
        
        return arr[0] 
        
    def recurse(self, node, arr):
        
        if node == None: return
        
        self.recurse(node.left, arr)
        arr.append(node)
        self.recurse(node.right, arr)

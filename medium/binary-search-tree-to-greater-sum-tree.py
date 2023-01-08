# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.far_left = None
        self.recurse(root)
        return root
    
    def recurse(self, node, parent=None):
        
        if node == None: 
            return
        
        self.recurse(node.right)

        if self.far_left != None:
            node.val += self.far_left
            if node.val > self.far_left:
                self.far_left = node.val
        else:
            self.far_left = node.val
            
            
        print(node.val)
        self.recurse(node.left)

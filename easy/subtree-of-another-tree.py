# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        if subRoot == None: return True
        tn= TreeNode(left=root)
        
        return self.recurse(root, subRoot)
    
    
    def recurse(self, node, sub):
        if node == None:
            return False
        
        
        if self.check_tree(node, sub): return True
        
        return self.recurse(node.left, sub) or self.recurse(node.right, sub)
        

        
        
    def check_tree(self, node, sub):
        if node == None and sub == None:
            return True
        elif node == None or sub == None: 
            return False
        
    
        return node.val == sub.val and (
            self.check_tree(node.left, sub.left) and self.check_tree(node.right, sub.right)
        )
         
        
        

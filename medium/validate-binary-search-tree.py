# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.smallest = -2147483648 - 10
        self.result = True
        
        self.dfs(root)
        
        return self.result
        
    def dfs(self, node): 
        if node is None: 
            return

        self.dfs(node.left)

        print(node.val, self.smallest)
        if node.val > self.smallest: 
            self.smallest = node.val
        else: 
            self.result = False
            return 

        self.dfs(node.right)
                    
        
        

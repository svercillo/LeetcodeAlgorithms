# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        

        inorder = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)
        print(inorder)
        

        x = None
        y = None
        for i in range(len(inorder)):
            if x is None and i < len(inorder) - 1 and inorder[i] > inorder[i+1]:
                x = inorder[i]
            elif i > 0 and inorder[i] < inorder[i-1]:
                y = inorder[i]
            

        def dfs(node, x, y):
            if not node:
                return
            if node.val == x:
                node.val = y
            elif node.val == y:
                node.val = x

            dfs(node.left, x, y)
            dfs(node.right, x, y)
        
        dfs(root, x, y)



            
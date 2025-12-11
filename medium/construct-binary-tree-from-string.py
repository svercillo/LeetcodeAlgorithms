# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        n = len(s)
        stack = [TreeNode(-1, TreeNode())]    
        i = 0
        while i < n:
            while i < n and s[i] == ")": 
                stack.pop()
                i += 1
            if i == n:
                break
            if s[i] == "(":
                i += 1


            carr = []
            while i < n and (s[i] == "-" or s[i].isnumeric()):
                carr.append(s[i])
                i += 1 
            

            v = int("".join(carr))
            node = TreeNode(v)

            if not stack[-1].left:
                stack[-1].left = node
            elif not stack[-1].right:
                stack[-1].right = node

            stack.append(node)

            
            
            if i < n and s[i] == "(":
                i += 1
        return stack[0].right
        

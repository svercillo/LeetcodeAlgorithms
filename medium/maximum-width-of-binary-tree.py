# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0)]        



        depth = 0
        mdiff = 0
        while len(q):    
            new_q = []


            width = q[-1][1] - q[0][1] + 1
            mdiff = max(mdiff, width)

            for node,  index in q:
                if node.left:
                    new_q.append((node.left, index * 2 ))
                
                if node.right:
                    print(index, index * 2 + 1)
                    new_q.append((node.right, index * 2  + 1))


            
            depth += 1
            q = new_q
        return mdiff


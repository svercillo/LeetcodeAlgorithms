# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# [1,2,3,4,5, null, null, 6]
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        
#         if root and root.left and root.left.left is None:
#             left = root.left
#             left.right = root
            
#             root.left = None
#             return left
        if not root:
            return None
        
        q = [root] 
        
        prev_left_node = None
        
        while len(q) > 0:
            print([v.val for v in q], prev_left_node)
            left_node = q.pop(0)
        
            
            new_q = [] 
            if left_node.left:
                new_q.append(left_node.left)
            if left_node.right:
                new_q.append(left_node.right)
            
            
            if prev_left_node is not None:
                if len(q) > 0:
                    right_node = q.pop(0)

                    right_node.left = None
                    right_node.right = None

                    left_node.left = right_node

                    left_node.right = prev_left_node
                else:
                    left_node.right = prev_left_node
                    left_node.left = None 
                
            else:
                left_node.right = None
                left_node.left = None
            
            prev_left_node = left_node
            q = new_q

        return prev_left_node
            
                
                
            
            

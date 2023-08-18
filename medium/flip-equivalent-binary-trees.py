# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def sortTree(node):
            if not node:
                return None

            left_node = node.left
            right_node = node.right

            if right_node and not left_node:
                node.left = right_node
                node.right = None
            elif left_node and right_node:
                if right_node.val < left_node.val:
                    node.left = right_node
                    node.right = left_node
                
            sortTree(node.left)
            sortTree(node.right)    
        
        sortTree(root1)
        sortTree(root2)

        def compareTrees(node1, node2):
            if not node1 and not node2:
                return True
            elif (not node1 and node2) or (node1 and not node2):
                return False
            elif node1.val != node2.val: 
                return False

            return compareTrees(node1.left, node2.left) and compareTrees(node1.right, node2.right)

            
        return compareTrees(root1, root2)

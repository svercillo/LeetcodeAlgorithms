# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        if not root:
            return []
        res = []
        to_delete = set(to_delete)
        def dfs(node, parent, direction):
            if not node: 
                return

            
            dfs(node.left, node, "L")
            dfs(node.right, node, "R")

            if node.val in to_delete:
                if parent:
                    if direction == "L":
                        parent.left = None
                    else:
                        parent.right = None
                

                if node.left and node.left.val not in to_delete:
                    res.append(node.left)

                if node.right and node.right.val not in to_delete:
                    res.append(node.right)
        

        dfs(root, None, "L")
        if root.val not in to_delete:
            res.append(root)
        return res

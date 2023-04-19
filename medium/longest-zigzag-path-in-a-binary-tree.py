# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        max_value = 0
        def longest_path(node, last_went_left, path_len):
            nonlocal max_value

            if not node:
                return path_len - 1

            if last_went_left:
                return max(
                    longest_path(node.right, False, path_len + 1),
                    longest_path(node.left, True, 1)
                )
            else:
                return max(
                    longest_path(node.left, True, path_len + 1),
                    longest_path(node.right, False, 1)
                )

        
        return max(
            longest_path(root, True, 0), 
            longest_path(root, False, 0)
        )

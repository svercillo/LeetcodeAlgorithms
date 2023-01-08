# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
from functools import lru_cache
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        highest_val = 0

        @lru_cache
        def valid_bst(node):
            if (
                (node.right and node.val >= node.right.val)
                or (node.left and node.val <= node.left.val)
            ):
                return False, -1, -1

            if node.left:
                left_bst, llowest, lhighest = valid_bst(node.left)
                if node.right:
                    right_bst, rlowest, rhighest = valid_bst(node.right)
                    if left_bst and right_bst and lhighest < node.val < rlowest:
                        return True, llowest, rhighest
                    else:
                        return False, -1, -1
                else: 
                    if left_bst and lhighest < node.val:
                        return True, llowest, node.val 
                    else:
                        return False, -1, -1
            elif node.right:
                right_bst, rlowest, rhighest = valid_bst(node.right)
                if right_bst and node.val < rlowest:
                    return True, node.val, rhighest
                else:
                    return False, -1, -1
            return True, node.val, node.val

        @lru_cache
        def max_sum_bst(node):
            nonlocal highest_val
            if not node:
                return 0

            ''' 4 choices:
                1. take only this node as total sum
                2. take this node plus left child max sum
                3. take this node plus right child max sum
                4. take this node plus both left and right child max sums
            '''

            max_sum = node.val + max_sum_bst(node.left) + max_sum_bst(node.right)
            if valid_bst(node)[0]:
                if max_sum > highest_val:
                    highest_val = max_sum
            else:
                max_sum = math.inf

            
            return max_sum


        max_sum_bst(root)
        return highest_val if highest_val != math.inf and highest_val > 0 else 0

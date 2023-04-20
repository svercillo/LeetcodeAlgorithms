# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        def largest_bst(node):

            if node.left:
                lmax, lmin, lsize = largest_bst(node.left)
                
                if node.right:
                    rmax, rmin, rsize = largest_bst(node.right)

                    if (
                        not (lmax < node.val < rmin)
                        or lmax == -1
                        or rmax == -1
                    ): # if not valid bst
                        return -1, -1, max(lsize, rsize)
                    else:
                        return rmax, lmin, lsize + 1 + rsize
                else:
                    if (
                        not (lmax < node.val)
                        or lmax == -1
                    ): # if not valid bst
                        return -1, -1, lsize
                    else:
                        return node.val, lmin, lsize + 1

            elif node.right:
                rmax, rmin, rsize = largest_bst(node.right)

                if (
                    not (node.val < rmin)
                    or rmax == -1
                ): # if not valid bst
                    return -1, -1, rsize
                else:
                    return rmax, node.val, rsize + 1
            
            else:
                return node.val, node.val, 1 # leaf node

        if not root:
            return 0

        return largest_bst(root)[2]
                

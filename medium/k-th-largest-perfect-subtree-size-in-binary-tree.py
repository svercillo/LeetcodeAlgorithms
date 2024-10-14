# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        
        sizes = []
        def sizeSubtree(node, sizes):

            if node is None:
                return 0

            lval = sizeSubtree(node.left, sizes)
            rval = sizeSubtree(node.right, sizes)

            if lval == rval != -1:
                subtreeSize = lval + rval + 1
                sizes.append(subtreeSize)
                return subtreeSize
            else:
                return -1

        sizeSubtree(root, sizes)
        if k > len(sizes):
            return -1
        sizes.sort(reverse=True)

        return sizes[k-1]

                

            
                

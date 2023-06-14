# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:   

        @cache
        def trees_from(n):
            if n == 1:
                return [TreeNode()]
            elif n ==3:
                return [TreeNode(0, TreeNode(), TreeNode())]
            elif n % 2 == 0:
                return []

            res = []
            for num_nodes in range(1, n -1, 2):
                # print(num_nodes, n - num_nodes-1 )
                left = trees_from(num_nodes)
                right = trees_from(n - num_nodes-1)

                for ltree in left:
                    for rtree in right:
                        res.append(TreeNode(0, ltree, rtree))

            return res

        return trees_from(n)

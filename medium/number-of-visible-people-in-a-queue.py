# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        num_nodes = 0
        def dfs(node: TreeNode):
            nonlocal num_nodes

            if not node:
                return 0, 0
            
            total_sum = node.val
            total_size = 1

            _sum_left, size_left = dfs(node.left)
            _sum_right, size_right = dfs(node.right)

            total_sum += _sum_left + _sum_right
            total_size += size_left + size_right

            average = total_sum // total_size
            
            if average == node.val: 
                num_nodes += 1


            return total_sum, total_size
        dfs(root)
        return num_nodes

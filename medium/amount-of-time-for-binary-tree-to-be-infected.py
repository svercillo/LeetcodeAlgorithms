# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        parents = {}
        node_map = {}

        def find_parent(node, last):
            if not node:
                return
            parents[node.val] = last
            node_map[node.val] = node

            find_parent(node.right, node)
            find_parent(node.left, node)

        find_parent(root, None)

        visited = set()

        def dfs(node, time):
            if not node:
                return time

            if node.val in visited:
                return time

            visited.add(node.val)

            lval = dfs(node.left, time + 1)
            rval = dfs(node.right, time + 1)

            parent = parents[node.val]
            pval = dfs(parent, time + 1)

            return max(lval, rval, pval)

        total_time = dfs(node_map[start], 0)

        return total_time - 1

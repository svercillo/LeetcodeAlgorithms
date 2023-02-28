# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        freq = collections.defaultdict(lambda: 0)
        visited = {}
        
        def dfs(node):
            if not node:
                return []
            
            tree = [str(node.val)]

            tree.append("L")
            tree.extend(dfs(node.left))

            tree.append("R")
            tree.extend(dfs(node.right))

            _id = ""
            for c in tree:
                _id += c

            visited[_id] = node
            freq[_id] += 1

            return tree

        dfs(root)


        return [visited[k] for k in visited if freq[k] >= 2]

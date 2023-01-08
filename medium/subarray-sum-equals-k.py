# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        

        if not root:
            return 0 

        res = 0
        def dfs(node, _min, _max):
            nonlocal res
            if not node:
                return

            if node.val < _min:
                _min = node.val
            elif node.val > _max:
                _max = node.val


            res = max(_max - _min, res)

            dfs(node.left, _min, _max)
            dfs(node.right, _min, _max)

        dfs(root, root.val, root.val)

        return res

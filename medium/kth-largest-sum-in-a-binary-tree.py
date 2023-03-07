# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        level_sums = []
        q = [root]

        while len(q):
            new_q = []
            level_sum = 0
            for n in q:
                if n: 
                    level_sum += n.val
                    new_q.append(n.left)
                    new_q.append(n.right)

            
            if level_sum:
                level_sums.append(level_sum)
            q = new_q

        # print(sorted(level_sums, reverse=True))
        return sorted(level_sums, reverse=True)[k -1] if k-1 < len(level_sums) else -1

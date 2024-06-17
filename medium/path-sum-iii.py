# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:

        if not root:
            return 0

        result = 0
        def possibleSums(node):
            nonlocal target, result
            possible = {}
            if node.left:
                possible = possibleSums(node.left)
            if node.right:
                right_sums = possibleSums(node.right)
                for k in right_sums:
                    if k not in possible: 
                        possible[k] = 0
                    possible[k] += right_sums[k]

            new_possible = {
                key + node.val: possible[key] for key in possible
            }
            
            if node.val not in new_possible:
                new_possible[node.val] = 0
            
            new_possible[node.val] += 1
            
            if target in new_possible: 
                result += new_possible[target]
            return new_possible

        
        possibleSums(root)

        return result
    


            



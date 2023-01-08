# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        max_seq = 0
        def dfs(node , parent, seq_length):
            
            nonlocal max_seq
            max_seq = max(max_seq, seq_length)   
            if not node:
                return
            
            
            if parent:
                # print(node.val, parent.val, seq_length)
                
                if parent.val + 1 == node.val:
                    seq_length +=1 
                else: 
                    seq_length = 1

            dfs(node.left, node, seq_length)
            dfs(node.right, node, seq_length)
            
        dfs(root, None, 1)
        
        return max_seq
        

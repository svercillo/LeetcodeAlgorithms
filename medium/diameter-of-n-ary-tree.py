"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        diameter = 0 
        
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            
            
            longest = 0
            secondlongest = 0
            for child in node.children:
                childsum = dfs(child)
                if childsum > longest:
                    secondlongest = longest
                    longest = childsum
                elif childsum > secondlongest:
                    secondlongest = childsum
            
            diameter = max(longest + secondlongest, diameter)

            return longest + 1

        dfs(root)
        return diameter

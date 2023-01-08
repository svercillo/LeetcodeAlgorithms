"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        
        
        n = len(tree)
        
        visited = {} 
        
        def dfs(node):
            
            if not node:
                return 0
            
            if id(node) in visited:
                return visited[id(node)]
                
            val = 1
            
            for child in node.children:
                val += dfs(child)
            
            
            visited[id(node)] = val
            
            return val
        
        for node in tree:
            res = dfs(node) 
            
            if res == n:
                return node
                
        

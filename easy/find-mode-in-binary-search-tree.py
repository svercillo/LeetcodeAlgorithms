# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.freq = {}
        self.dfs(root)        
        
        
        max_val = -1
        for k in self.freq:
            if self.freq[k] > max_val:
                max_val = self.freq[k]
        
        res = []
        for k in self.freq:
            if self.freq[k] == max_val:
                res.append(k)
                
        return res

            
        

        
    def dfs(self, node): 
        if node is None: 
            return

        self.dfs(node.left)

        if node.val not in self.freq:
            self.freq[node.val] = 1
        else: 
            self.freq[node.val] += 1

        self.dfs(node.right)
                    
        
        

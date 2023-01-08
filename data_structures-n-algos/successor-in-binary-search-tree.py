# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        
        
        path = [(root, "")]
        def dfs(node, path):
            nonlocal p
            
            
            if node.val == p.val:
                
                if not node.right:
                    while len(path) > 0:
                        parent, direction = path.pop()

                        if direction == "":
                            if node.val < root.val:
                                return node

                            if node.val == root.val: 
                                if root.right: 
                                    nxt = root.right
                                    while nxt.left:
                                        nxt = nxt.left

                                    return nxt
                                else: 
                                    return  None
                            else: 
                                return None
                        elif direction == "l":
                            return parent
                        else: # direction right
                            pass
                    
                else:
                    nxt = node.right
                    
                    while nxt.left:
                        nxt = nxt.left
                        
                    return nxt
                    
            elif node.val > p.val:
                path.append((node, 'l'))
                return dfs(node.left, path)
            else:
                path.append((node, 'r'))
                return dfs(node.right, path)
                
            
            
            
        return dfs(root, path)

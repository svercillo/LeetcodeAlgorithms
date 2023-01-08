# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        res = [root.val]
        q = [root]
        
     
        leaves = []

        max_height = 0
        while len(q): 
            max_height += 1
            row = []
        
            for node in q:
                if node.left:
                    row.append(node.left)
                    
                if node.right:
                    row.append(node.right)
                    

            q = row
        max_height -=1
            
        
        
        def dfs(node, height, left, res):
   
            if 0 < height:
                print(height, max_height)
                res.append(node.val)
            if left:
                if node.left:
                    dfs(node.left, height+1, left, res)
                elif node.right:
                    dfs(node.right, height +1, left,res )
            else:
                if node.right:
                    dfs(node.right, height+1, left, res )
                elif node.left: 
                    dfs(node.left, height+1, left, res)
        
        def full_dfs(node, height, full_left, full_right):
            print(node.val, full_left, full_right)
            if not full_left and not full_right and not node.left and not node.right:
                leaves.append(node.val)
            
            if node.left and node.right:
                full_dfs(node.left, height+1, full_left, False)
                full_dfs(node.right, height+1, False, full_right)
            elif node.left or node.right:
                if node.left:
                    full_dfs(node.left, height+1, full_left, full_right)
                else:
                    full_dfs(node.right, height+1, full_left, full_right)
            

        
        
        
        left_boundary = []
        if root.left: 
            full_dfs(root.left, 0, True, False)
            dfs(root, 0, left=True, res=left_boundary)
        print(left_boundary)
        
        
        right_boundary = [] 
        if root.right:
            full_dfs(root.right, 0, False, True)
            dfs(root, 0, left=False, res=right_boundary)
        
        print(right_boundary)
        res.extend(left_boundary)
        
        print("leaves", leaves)
        
        res.extend([l for l in leaves])
        
        res.extend(right_boundary[::-1])
            
        return res            
        
            
        
        
        

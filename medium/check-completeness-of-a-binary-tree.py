# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        q = [root]
                
        first_skipped = False
        while len(q) != 0: 
            print([(a.val if a is not None else "none") for a in q  ])
            row = []
            
            while len(q) != 0: 
                
                ele = q.pop(0)
                
                if ele is None: 
                    first_skipped = True
                    continue
                elif first_skipped:
                    return False
                # print(ele.val)
                row.append(ele.left)
                row.append(ele.right)
                
            q.extend(row)
        return True
            
            

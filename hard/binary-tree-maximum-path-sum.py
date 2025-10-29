# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        class Answer:
            def __init__(self, val):
                self.set = False
                self.val = val
        answer = Answer(0)

        # idea: each node return max left and max right
        def maxSum(node):
            mleft, mright = 0, 0
            if node.left: 
                l, r = maxSum(node.left)
                mleft = max(l, r) + node.val
    
            if node.right:
                l, r = maxSum(node.right)
                mright = max(l, r) + node.val
    
    
            mleft = max(mleft, node.val, 0)
            mright = max(mright, node.val, 0)

            # print(node.val, (mleft, mright))


            if mleft == 0 and mright == 0:
                if not answer.set:
                    answer.val = node.val
                    answer.set = True
                elif node.val > answer.val:
                    answer.val = node.val
                return (0,0)    
            elif mleft == 0 or mright ==0: 
                
                if mleft + mright > answer.val:
                    answer.val = mleft + mright
                    answer.set = True
            else:
                if mleft + mright - node.val > answer.val:
                    answer.val = mleft + mright - node.val
                    answer.set = True

            return (mleft, mright)
        

        maxSum(root)

        return answer.val
            

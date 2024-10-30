# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        colMapping = {}
        def traverse(node, row, col):
            if col not in colMapping:
                colMapping[col] = {}
            
            if row not in colMapping[col]:
                colMapping[col][row] = []
            
            colMapping[col][row].append(node.val)

            if node.left:
                traverse(node.left, row + 1, col -1)

            if node.right:
                traverse(node.right, row + 1, col +1)



        traverse(root, 0, 0)

        res = []
        for col in sorted([col for col in colMapping]):

            colVals = []
            for row in sorted([row for row in colMapping[col]]):
                colMapping[col][row].sort()
                for node in colMapping[col][row]:
                    colVals.append(node)
                    




            res.append(colVals)



        # print(colMapping)

        return res

        

            

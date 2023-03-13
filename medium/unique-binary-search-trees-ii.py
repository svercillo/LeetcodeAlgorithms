# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def num_trees(start, end): # returns the number of trees from start to end

            print(start, end)
            if start > end:
                return []
            
            elif end == start:
                return [TreeNode(end)]

            res = []
            for val in range(start, end +1):
                print(val)

                left_trees = num_trees(start, val-1)
                right_trees = num_trees(val + 1, end)

                nl = len(left_trees)
                nr = len(right_trees)

                if nl == 0: # special case can't combine in for loop
                    for j in range(nr):
                        mid = TreeNode(val)
                        mid.right = right_trees[j]
                        res.append(mid)


                elif nr == 0: # special case
                    for i in range(nl):
                        mid = TreeNode(val)
                        mid.left = left_trees[i] 
                        res.append(mid)
                else:
                    # add every combination of left and right trees
                    for i in range(nl):
                        for j in range(nr):
                            mid = TreeNode(val)
                            mid.left = left_trees[i]
                            mid.right = right_trees[j]                
                            res.append(mid)
            

            return res


        res = num_trees(1, n)
        return res

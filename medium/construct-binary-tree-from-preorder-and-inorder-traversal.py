# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        positions = {}
        for i, node in enumerate(inorder):
            positions[node] = i

        root = None        

        def dfs(lp, rp):
            if lp > rp:
                return None
            top = preorder.pop(0)
            node = TreeNode(top)

            pos = positions[top]
            print(top, lp, rp)

            if len(preorder):
                next_top = preorder[0]
                next_pos = positions[next_top]

                if next_pos < lp or next_pos > rp:
                    return node 

                if next_pos > pos:
                    # rhs first
                    node.right = dfs(pos + 1, rp)
                    
                else:
                    # lhs first
                    node.left = dfs(lp, pos -1)


                if len(preorder) > 0: 
                    print(lp, pos -1)
                    if next_pos > pos:
                        node.left = dfs(lp, pos -1)
                    else:
                        node.right = dfs(pos + 1, rp)

            return node
        
        # return dfs([0] * n)
        return dfs(0, n-1)
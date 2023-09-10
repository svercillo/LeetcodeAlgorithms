# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parents = {}


        def set_parents(node, parent, parents):
            if not node:
                return


            parents[id(node)] = parent
            
            set_parents(node.left, node, parents)
            set_parents(node.right, node, parents)
        set_parents(root, None, parents)
        

        q = [target]

        visited = set([id(target)])
        while len(q) and k:
            new_q = []
            for node in q:
                for neigh in [node.left, node.right, parents[id(node)]]:
                    if neigh and id(neigh) not in visited:
                        new_q.append(neigh)
                        visited.add(id(neigh))
            
            k -= 1
            q = new_q
        
        if k:
            return []

        return [node.val for node in q]

            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def lowestCommonAncestor(root, p: int,  q: int):

    lca = None

    def dfs(node):
        nonlocal p, q, lca

        if not node or lca:
            return False, False

        containsp = False
        containsq = False


        res1 = dfs(node.left)
        res2 = dfs(node.right)

        containsp = containsp or res1[0] or res2[0]
        containsq = containsq or res1[1] or res2[1]


        if node.val == p:
            containsp = True
        elif node.val == q: 
            containsq = True

        # print(node.val, containsp, containsq)

        if containsp and containsq and not lca: 
            lca = node    

        return containsp, containsq
    
    dfs(root)

    return lca

class Solution:
    def getDirections(self, root: Optional[TreeNode], src: int, dest: int) -> str:
        
        
        lca = lowestCommonAncestor(root, src, dest)

        
        def getPath(node, target, path):
            
            if not node or (len(path) and path[-1] == -1):
                return
            
            # print(node.val, path, target)
            
            if node.val == target:
                path.append(-1)
                return
            
            path.append("L")
            getPath(node.left, target, path)
            if path[-1] != -1:
                path.pop()
            else:    
                return
            

            path.append("R")
            getPath(node.right, target, path)
            if path[-1] != -1:
                path.pop()
            else:
                return
            
        srcpath = deque()
        getPath(lca, src, srcpath)
        
        destpath = deque()
        getPath(lca, dest, destpath)
        
        res = ""
        for i, ele in enumerate(srcpath):
            if i < len(srcpath) -1:
                res += "U"
            
        for i, ele in enumerate(destpath):
            if i < len(destpath) -1:
                res += ele
            
        return res

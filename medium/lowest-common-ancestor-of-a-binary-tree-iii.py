"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        cache = {}
        savecache = False
        
        def recurse(node):
            nonlocal p, q, cache, savecache, isp
            if not node:
                return 0
            
            if savecache:
                if node.val in cache:
                    if cache[node.val] != isp:
                        return 2
                    else:
                        return 0
                cache[node.val] = isp
            

            val = 0
            val += recurse(node.left)
            val += recurse(node.right)
            
            
            if node.val == p.val and node.val == q.val:
                val += 2
            elif node.val == p.val or node.val == q.val:
                val += 1
                
            return val

        res1 = recurse(q)
        if res1 >= 2:
            return q
        
        res2 = recurse(p)
        if res2 >= 2:
            return p

        failed = set()
        
        p1 = p.parent
        p2 = q.parent
        
        isp = True
        savecache = True
        while p1 != None and p2 != None:
            if isp:
                res = recurse(p1)
                if res >= 2:
                    return p1
                p1 = p1.parent
            else:
                res = recurse(p2)
                if res >= 2: 
                    return p2
                p2 = p2.parent
                
            isp = not isp
            

        while p1 != None:
            res = recurse(p1)
            if res >= 2:
                return p1

            p1 = p1.parent
            
        while p2 != None:
            res = recurse(p2)
            if res >= 2:
                return p2
            
            p2 = p2.parent
            
        return None

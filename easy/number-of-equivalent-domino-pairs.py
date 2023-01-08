from math import comb
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dom = dominoes
        n = len(dom)
        num = 0
        
        doms = {}
        
        
        for d in dom: 
            t = tuple(sorted(d))
            
            if t in doms:
                doms[t] += 1
            else:
                doms[t] = 1
                
        
        tot = 0
        for t in doms: 
            tot += comb(doms[t], 2)
        
        return tot

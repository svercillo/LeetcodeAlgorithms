class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        s1, s2 = set(), set()
        
        for c in source:
            s1.add(c)
            
        for c in target:
            s2.add(c)
            
            
        for c in s2: # check if extra chars present
            if c not in s1:
                return -1
            
        
        n, m = len(source), len(target)
        
        
        
        p1 = 0
        p2 = 0 
        
        count = 1
        while p2 < m:
            while p1 < n and source[p1] != target[p2]:
                p1 += 1
            
                
            if p1 == n:
                count +=1
                p1 = 0
                continue
                
            p1 += 1
            p2 += 1
            
        return count

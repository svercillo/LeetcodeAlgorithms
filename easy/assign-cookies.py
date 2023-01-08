class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        p1 = 0 
        p2 = 0
        count = 0
    
        while p1 < len(g) and p2 < len(s):
            
            
            while p2 <len(s) and s[p2] < g[p1]:
                p2 +=1
            
            if p2 < len(s):
                count +=1
            
            p1 += 1 
            p2 += 1
        return count

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        n = len(s)

        c1 = 0
        for i in range(floor(n/2)):
            if s[i] in v: c1 +=1
        
        

        for i in range(n-1, floor((n-1)/2), -1 ):
            if s[i] in v: c1 -=1
        
            
            
        return c1 ==0

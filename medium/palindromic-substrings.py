class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] *n ] * n
        
        count = 0
        # bottom up
        
        
        def recurse_odd(ind):
            nonlocal count 
            l, r = ind, ind #odd case
            
            while 0 <= l < n and 0 <=  r < n and s[l] == s[r]:
                count += 1

                l -=1
                r += 1
       
    
        def recurse_even(ind):
            nonlocal count 
            l, r = ind, ind +1 #odd case
            
            while 0 <= l < n and 0 <=  r < n and s[l] == s[r]:
                count += 1

                l -=1
                r += 1
                   
        for i in range(n):
            recurse_odd(i)
            if i != n-1:
                recurse_even(i)
        
            
        return count

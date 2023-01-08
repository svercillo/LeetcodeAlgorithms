class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        
        lf = {}
        for c in s:
            if c not in lf:
                lf[c] = 0
            
            lf[c] += 1
            
        
        num_odd = 0
        for c in lf:
            if lf[c] %2 == 1:
                num_odd +=1
                if num_odd > 1:
                    return False
                
        return True
            
            

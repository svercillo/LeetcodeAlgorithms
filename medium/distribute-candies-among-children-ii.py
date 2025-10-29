class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        total = 0
        for first in range(min(n +1, limit +1)):
            remaining = n - first

            if remaining > limit * 2:
                continue

            if limit >= remaining:
                total += remaining + 1
            else:
                total += 2* limit - remaining + 1

            
        return total 
                
            

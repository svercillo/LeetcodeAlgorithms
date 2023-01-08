class Solution:
    def mySqrt(self, x: int) -> int:
        
        val = x
        
        while val * val > x:
            val  //= 2
        
        
        
        while val * val <= x: 
            val += 1
        
        
        val -=1
        return val

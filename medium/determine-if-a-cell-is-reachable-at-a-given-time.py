class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        diff1 = abs(sx - fx)
        diff2 = abs(sy - fy)
        
        
        
        if (sx, sy) == (fx, fy) and t == 1:
            return False
        
        
        if max(diff1, diff2) <= t:
            return True
        

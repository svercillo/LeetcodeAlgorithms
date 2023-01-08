class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        if not len(ops):
            return m * n
            
        min_x, min_y = math.inf, math.inf
        for x, y in ops:
            min_x = min(min_x, x)
            min_y = min(min_y, y)

        return int(min_x * min_y) 


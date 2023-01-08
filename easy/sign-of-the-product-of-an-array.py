class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        pos = 1
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                pos = 1 if pos == -1 else -1
                
        return pos

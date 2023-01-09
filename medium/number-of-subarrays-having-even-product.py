class Solution:
    def evenProduct(self, nums: List[int]) -> int:  
        total = 0
        last_even = None
        for i, e in enumerate(nums):
            if e % 2 == 0:
                last_even = i
                total += i + 1
            elif last_even is not None:
                total += last_even+1        
        return total

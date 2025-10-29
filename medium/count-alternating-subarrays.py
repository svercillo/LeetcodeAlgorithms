class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        i=0
        n = len(nums)
        
        res = 0
        start = None 
        while i < n:
            if start is None or  (start % 2 ^ i % 2) != (nums[start] % 2 ^ nums[i] % 2):
                start = i
            res += i - start + 1
            i += 1

        return res

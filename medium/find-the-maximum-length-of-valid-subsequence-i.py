class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # skip adj numbers that have the same % 2
        nums = [e % 2 for e in nums]
             
        num_odd = nums.count(1)
        num_even = nums.count(0)
        
        
        switches = 0
        last = nums[0]
        for e in nums:
            if e != last:
                switches += 1
                
            last = e
            
        
        return max(num_odd, num_even, switches + 1)

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        
        highest_even = -1
        while i < n:
            val = nums[i]
            
            if val % 2 == 0:
                # print(val, i)
                if i > highest_even + 1: # non adjacent, => need swap
                    nums[i] = nums[highest_even + 1]
                    nums[highest_even+1] = val
                # print(nums)
                highest_even += 1 
            
            i += 1 
        
        return nums
            
            

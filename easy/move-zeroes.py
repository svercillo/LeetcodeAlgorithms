class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        count = 0 
        for i in range(n):
            if nums[i] != 0:
                nums[i - count] = nums[i]                
            else:
                count += 1
        
        
        for i in range(n-1, n -1 - count, -1):
            nums[i] = 0 
            
            
                
            

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        
        
        
        first = nums[len(nums) -1] * nums[len(nums) -2] * nums[len(nums) -3]
        sec = nums[0] * nums[1] * nums[len(nums) -1]
        
        
        
        return max(first, sec)
        

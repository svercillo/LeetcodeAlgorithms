class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        to_delete = []
        for i in range(len(nums) -2, -1, -1):
            if nums[i] == nums[i+1]:
                to_delete.append(i)
            
        for d in to_delete:
            nums.pop(d)
        
        
        return len(nums)

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        gte = True

        for i in range(n -1):
            if (nums[i +1] >= nums[i]) != gte:
                t = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = t
            gte = not gte

        

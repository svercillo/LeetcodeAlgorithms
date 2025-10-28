class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        if  1 not in nums: 
            return 1
        
        for i,e in enumerate(nums):
            if e <= 0:
                nums[i] = 1

        for i,e in enumerate(nums):
            # print(i, e)
            if abs(e) -1 < len(nums):
                # print("sdfsdf")
                nums[abs(e)-1] = -abs(nums[abs(e) -1])
                

            # print(nums)
        
        print(nums)    
        for i in range(n):
            if nums[i] >= 0: 
                return i+ 1

        
        return n + 1



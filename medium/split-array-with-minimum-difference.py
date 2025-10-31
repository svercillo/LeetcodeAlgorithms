class Solution:
    def splitArray(self, nums: List[int]) -> int:

        nums = [-1] + nums + [-1]
        n = len(nums)

        eqmiddle = False
        goingup = True
        middle = None
        for i in range(n-1):
            if goingup:
                if nums[i] == nums[i+1]:
                    eqmiddle = True
                
                if nums[i] >= nums[i+1]:    
                    goingup = False
                    middle = i # offset at the begginning
                    
            else:
                if nums[i] <= nums[i+1]:
                    return -1
                
                

        if not middle: 
            return -2 
        

        if eqmiddle:
            print(nums[1:middle+1], nums[middle+1:-1])
            return abs(sum(nums[1:middle+1]) - (sum(nums[middle+1:-1])))


        
        return min(
            abs(sum(nums[1:middle]) + nums[middle] - sum(nums[middle+1:-1])),
            abs(sum(nums[1:middle]) - (nums[middle] + sum(nums[middle+1:-1])))
        )
        
            
                ©leetcode

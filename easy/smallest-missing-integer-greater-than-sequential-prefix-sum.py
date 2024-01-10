class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return nums[0]
        
        last = nums[0] -1
        
        x = sum(nums)
        for index in range(len(nums)):
            e = nums[index]
            if last + 1 != e:
                x =  ((last + 1) * last // 2) - ( (nums[0] -1) * nums[0] // 2)
                break
                
            last = e
        

        for i in range(len(nums)):
            e = abs(nums[i])
            if e >= x:
                ind = e -x
                if ind < len(nums) and nums[ind] > 0: 
                    
                    nums[ind] *= -1
            

        count_in_seq = len(nums)
        for i in range(len(nums)): 
            e = nums[i] 
            if e >= 0:
                count_in_seq = i
                break
                
        return count_in_seq + x 

                    
        
        
    

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
        e_sum = 0 # even sum
        o_sum = 0 # odd sum
        
        e_sum2 = 0 # even sum
        o_sum2 = 0 # odd sum
    
    
        dp = [[]] * len(nums)
        
    
        for i in range(len(nums)):
            if i %2 == 0:
                e_sum += nums[i]
            else:
                o_sum += nums[i]
            
            j = len(nums)-1 -i
            
            if j %2 ==0:
                e_sum2 += nums[j]
            else:
                o_sum2 += nums[j]
                
            dp[i] = [e_sum, o_sum, e_sum2, o_sum2]
            
        count = 0
        for i in range(len(nums)):
                       
            j = len(nums)-1 -i
            if dp[i][0] + dp[j][3] == dp[i][1] + dp[j][2]:
                count +=1        
                       
        return count 
        
                
        
                
                
        
                
                
            
            
            
            

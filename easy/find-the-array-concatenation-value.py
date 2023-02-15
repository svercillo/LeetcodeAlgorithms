class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        lp, rp = 0, n-1
        
        
        
        
        res = 0
        while lp <= rp:
            
            string = str(nums[lp])
            
            if rp != lp:
                string += str(nums[rp])
                
            lp += 1
            rp -=1
        
        
            res += int(string)
        
            
        
        return res
            

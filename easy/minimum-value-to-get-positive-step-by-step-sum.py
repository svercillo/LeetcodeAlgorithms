class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        
        min_val = math.inf 
        res =0
        for n in nums: 
            res += n
            
            if res < min_val:
                min_val = res
                
        if min_val >=0: 
            return 1
        
        return abs(min_val) +1 
             

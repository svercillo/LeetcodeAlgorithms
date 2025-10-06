class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    
        values = set(nums)  


        _sum = sum(nums) 

        for v in values:
            total = v
            for v2 in values:
                if v2 == v:
                    continue
                total += v2 *3 
        
            if total == _sum:
                return v

        return -1

        

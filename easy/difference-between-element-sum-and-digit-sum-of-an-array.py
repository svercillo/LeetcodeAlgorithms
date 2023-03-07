class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        esum, dsum = 0,0
        for e in nums: 
            
            string = str(e)
            esum += e
            for c in string:
                dsum += int(c)
                
                
        return abs(esum - dsum)
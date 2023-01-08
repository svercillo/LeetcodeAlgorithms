class Solution:
    
    def largestNumber(self, nums) -> str:
        nums = [str(n) for n in nums] 
        class Comparator(str):
            def __lt__(self, that):
                
                return (self + that) < (that + self)

        nums.sort(key=Comparator, reverse=True)
        
        first = True
        res = "" 
        zero = False
        for n in nums:
            if first and n == "0": 
                zero = True
                continue
            res += n
            
            first = False
            
        if res == "" and zero:
            return "0"
        
        return res

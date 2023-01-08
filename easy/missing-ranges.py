class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        n = len(nums)
        
        
        if n == 0:
            return [str(lower)] if lower == upper else [f"{lower}->{upper}"]
        
        res = []
        
        
            
        start = None
        for c in nums:
            if lower < c <= upper:
                if not start:
                    start = lower
                if c -1 - start > 0:
                    res.append(f"{start}->{c-1}")
                elif c-1 - start == 0:
                    res.append(f"{c-1}")

            start = c + + 1
        
        print(start)
        if start <= upper:
            if upper - start >= 1:
                res.append(f"{start}->{upper}")
            else:
                res.append(str(upper))
                        
                    
        return res 
            
            

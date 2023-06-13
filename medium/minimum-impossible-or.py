class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        res = set()
        for e in nums:
            if abs(math.log(e, 2) % 1 - 0) < 10 ** -7:
                res.add(e)
            
        value = 1

        res = sorted([r for r in res])

        for e in res:
            if e != value:
                return value

            value *= 2 
        
        return value

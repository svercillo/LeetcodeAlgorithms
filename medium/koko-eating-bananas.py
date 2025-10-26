class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def condition(k):
            nhours = 0
            for p in piles:
                nhours += math.ceil(p / k)

            if nhours <= h: 
                return True
            
        
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2

            if condition(m):
                r = m
            else: 
                l = m + 1

        return l

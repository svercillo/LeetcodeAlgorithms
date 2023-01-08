class Solution:
    def solve(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        small = prices[0]


        total = 0
        for i, e in enumerate(prices):
            
            if e < small: 
                small = e
            
            if e > small:
                total += e - small
                small = e

        
        return total
            

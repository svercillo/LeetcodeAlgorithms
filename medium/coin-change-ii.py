import math
import bisect
from functools import cache
class Solution:
    def change(self, amount: int, coins) -> int:
        coins.sort()

        if not amount:
            return 1

        @cache
        def numways(value, cind):
            if value == 0:
                return 1
            
            if value < 0:
                return 0

            if cind >= len(coins):
                return 0
            
            c = coins[cind]
            maxfreq = math.floor(value / c)

            total = 0
            for f in range(0, maxfreq +1):
                rem = value - c * f
                total += numways(rem, cind + 1)

            return total
            
        total = numways(amount, 0)

        return total
        

from functools import lru_cache
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @lru_cache
        def get_power(x):
            if x == 1:
                return 0
            if x % 2 == 0:
                return get_power(x/2) + 1 
            else:
                return get_power(3*x + 1) +1

        
        powers = []
        for num in range(lo, hi +1): 
            powers.append((num, get_power(num)))

        powers.sort(key = lambda k: (k[1],k[0]))
        print(powers)

        return powers[k-1][0]

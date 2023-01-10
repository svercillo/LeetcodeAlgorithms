class Solution:
    def countGoodStrings(self, low: int, high: int, incrzeros: int, incrones: int) -> int:

        @lru_cache(None)
        def num_good_strings(stringlen):
            nonlocal low, high, incrzeros, incrones

            total = 0
            if stringlen > high:
                return 0

            if stringlen >= low:
                total += 1
            
            
            total += num_good_strings(stringlen + incrzeros) % (10 ** 9 + 7)
            total += num_good_strings(stringlen + incrones) % (10 ** 9 + 7)

            return total

        return num_good_strings(0) % (10**9 + 7)
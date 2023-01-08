from functools import cache
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        @cache
        def dfs(num_dice, target):
            nonlocal k
            
            if num_dice == 1:
                return 1 if 1 <= target <= k else 0 # base case
              
            num_ways = 0
            for i in range(1, k +1):
                if target-i >= 1:
                    num_ways += dfs(num_dice-1, target-i)
                    num_ways %= 10**9 + 7
                else:
                    break

            return num_ways

        return dfs(n, target) % (10**9 + 7)

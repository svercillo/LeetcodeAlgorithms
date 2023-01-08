from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        @lru_cache
        def dfs(i, holding):
            nonlocal fee
            if i >= len(prices):
                return 0

            profit = 0
            if holding:
                # can sell or not sell
                profit = max(prices[i] - fee + dfs(i+1, False), dfs(i+1, True))
            else:
                # can buy or not buy
                profit = max(-prices[i] + dfs(i+1, True), dfs(i+1, False))
            return profit
        return dfs(0,False)

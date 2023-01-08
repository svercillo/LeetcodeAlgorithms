from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache
        def recurse(i, holding, cooldown=False):
            if i >= len(prices): 
                return 0
            
            profit = 0
            if holding:
                # can sell or not sell
                profit = max(
                    profit, prices[i] + recurse(i+1, False, True), recurse(i+1, True)
                )

            else:
                if not cooldown: 
                    # can buy or not buy
                    profit = max(
                        profit, recurse(i+1, True) - prices[i], recurse(i+1, False)
                    )
                else:
                    # can't buy, do nothing. cool down is set to 0
                    profit = max(profit, recurse(i +1, False))
            return profit
                
        return recurse(0, False, False)
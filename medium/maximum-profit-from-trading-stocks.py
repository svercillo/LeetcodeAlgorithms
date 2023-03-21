class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        

        cache = []
        for i in range(len(present)):
            row = []
            for j in range(budget+1):
                row.append(-1)

            cache.append(row)

        def max_profit(ind, budget): # returns the max profit for up to the ind th stock
            if cache[ind][budget] != -1:
                return cache[ind][budget]


            n = len(present)

            if ind < 0:
                return 0
            
            
            mprofit = 0
            if budget >= present[ind]: # if have enough money
                # take stock    
                curr_profit = future[ind] - present[ind]
                mprofit = max(
                    max_profit(ind-1, budget- present[ind]) + curr_profit,
                    mprofit   
                )

            # don't take stock 
            mprofit = max(
                max_profit(ind-1, budget),
                mprofit
            )


            cache[ind][budget] = mprofit
            return mprofit



        return max_profit(len(present)-1, budget)

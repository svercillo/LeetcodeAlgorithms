import math
from functools import cache
class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:

        n = len(express)
        regular_cost = [math.inf] * n
        express_cost = [math.inf] * n

        @cache
        def min_cost(stop_ind, onExpress): # min cost to get to stop_ind from stop 0
            if stop_ind == -1:
                if onExpress:
                    return expressCost # can't start on express
                else:
                    return 0 # base case

            
            # cost to get to stop_ind == (cost of stop_ind-1 + transit cost)
            cost = math.inf
            if onExpress: 
                cost = min(                    
                    min_cost(stop_ind-1, True) + express[stop_ind], # continue on express
                    min_cost(stop_ind-1, False) + expressCost + express[stop_ind] # switch from regular to express
                )
            else:
                cost = min(
                    min_cost(stop_ind-1, True) + regular[stop_ind], # switch from express to regular
                    min_cost(stop_ind-1, False) + regular[stop_ind]  # stay on regular 
                )
            return cost

        res = []
        for ind in range(0, n):    
            res.append(
                min(
                    min_cost(ind, True),
                    min_cost(ind, False)
                )
            )

        return res
        
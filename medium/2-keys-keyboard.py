from functools import lru_cache
class Solution:
    def minSteps(self, n: int) -> int:

        
        @lru_cache
        def dfs(astring, clipboard):
            if astring == n:
                return 0
            elif astring > n:
                return math.inf


            min_cost = math.inf
            # two choices, print or copy
            # print
            if clipboard != 0: 
                min_cost = dfs(astring + clipboard, clipboard) + 1
            
            # copy 
            if astring > clipboard:
                min_cost = min(min_cost, dfs(astring, astring) + 1)

            return min_cost

        return dfs(1, 0)

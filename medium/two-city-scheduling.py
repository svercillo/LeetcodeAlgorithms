class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        @cache
        def minCost(i, numA):
            nonlocal n
            if i == n:
                return 0 if numA == n // 2 else math.inf
            return min(
                minCost(i + 1, numA + 1) + costs[i][0],
                minCost(i + 1, numA) + costs[i][1]
            )



        
        return minCost(0, 0)

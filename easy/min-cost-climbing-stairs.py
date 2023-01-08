class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1) 

        dp[0] = (cost[0], 0)
        dp[1] = (cost[1], cost[0])

        for i in range(2, n):
            dp[i] = [-1, -1]

            # take
            dp[i][0] = cost[i] + min(dp[i-1][0], dp[i-1][1])

            # don't take 
            dp[i][1] = dp[i-1][0]
        
        return min(dp[n-1])
        

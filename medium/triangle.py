class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        i = n - 2
        dp = triangle[n-1]

        while i >= 0:
            m = len(triangle[i])
            new_dp = [-1] * m
            
            for j in range(m):
                new_dp[j] = min(dp[j], dp[j+1]) + triangle[i][j] 

            dp = new_dp
            i -= 1
        return dp[0]

class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [-1] * (n + 1 )
        def num_ways(n):
            
            if n == 0:
                return 1
            elif n == 1:
                return 1

            if dp[n] != -1: 
                return dp[n]
            

            val = 0 
            for i in range(n):
                val += num_ways(i) * num_ways(n - 1 - i)
            
            dp[n] = val
            return val


        return num_ways(n)

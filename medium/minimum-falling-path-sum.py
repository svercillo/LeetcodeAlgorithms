class Solution:        
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(-1)
            dp.append(row)
        

        def dfs(i, j):
            nonlocal n
            if i == n -1:
                return matrix[i][j]

            if dp[i][j] != -1:
                return dp[i][j]
            
            arr  = []
            for k in range(-1, 2):
                tj = j + k

                if 0 <= tj < n:
                    arr.append(dfs(i+1, tj))
                    
            dp[i][j] = min(arr) + matrix[i][j]

            return dp[i][j]

        return min([dfs(0,i) for i in range(n)])

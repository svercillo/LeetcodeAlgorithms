class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        dirs = [
            [1,0],
            [0,1],
            [-1,0],
            [0,-1]
        ]
        
        def dfs(i, j):
            if (i, j) in visited:
                return visited[(i,j)]

            longest_train = 0
            for down, right in dirs:
                ti = i + down
                tj = j + right

                if (
                    0 <= ti < n 
                    and 0 <= tj < m
                    and matrix[i][j] < matrix[ti][tj]
                ): 
                    longest_train = max(longest_train, dfs(ti, tj))
            
            visited[(i, j)] = longest_train + 1
            return longest_train + 1

        longest_train = 0
        visited = {}
        for i in range(n):
            for j in range(m):
                longest_train = max(longest_train, dfs(i, j))

        return longest_train

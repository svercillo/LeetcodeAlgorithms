class Solution:
    def countPaths(self, matrix: List[List[int]]) -> int:


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

            num_paths = 0
            for down, right in dirs:
                ti = i + down
                tj = j + right

                if (
                    0 <= ti < n 
                    and 0 <= tj < m
                    and matrix[i][j] < matrix[ti][tj]
                ): 
                    num_paths += dfs(ti, tj)
                                
            visited[(i, j)] = num_paths + 1
            return num_paths + 1
        visited = {}
        for i in range(n):
            for j in range(m):
                dfs(i,j)

        
        total_num = 0 
        for i in range(n):
            for j in range(m):
                if (i,j) in visited:
                    total_num += visited[(i,j)]
        

        return total_num % (10 ** 9 + 7)

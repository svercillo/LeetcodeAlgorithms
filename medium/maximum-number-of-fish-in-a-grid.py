class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
    
        dirs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]


        visited = set()
        
        def dfs(i, j):
            nonlocal n, m

            if (i, j) in visited:
                return 0
            visited.add((i,j))
            
            total = grid[i][j]
            for down, right in dirs:
                ti = i + down
                tj = j + right

                if not (0 <= ti < n and 0 <= tj < m) or grid[ti][tj] == 0:
                    continue

                total += dfs(ti, tj)

            return total

        mvalue = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                
                value = dfs(i, j)
                mvalue = max(mvalue, value)


        return mvalue

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        mcount = 0

        visited = set()
        def dfs(i,j):
            nonlocal mcount
            if (i,j) in visited:
                return            

            visited.add((i,j))

            count[0] = count[0] + 1
            mcount = max(count[0], mcount)
            for down, right in directions:
                ti, tj = i+ down, j + right

                if 0<= ti < n and 0 <= tj <m and grid[ti][tj] == 1:
                    dfs(ti,tj)
                    
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: 
                    count = [0]
                    dfs(i, j)

        return mcount

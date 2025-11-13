class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [
            [0,1],
            [0, -1],
            [1, 0],
            [-1,0]
        ]

        q = []

        containswater = False
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i,j))
                else:
                    containswater = True

        if not containswater:
            return -1
        

        visited = set()
        count = 0
        while len(q):
            nq = []
            for i, j in q:
                for down, right in dirs:
                    ti = i + down
                    tj = j + right

                    if not (0<= ti < n and 0<= tj < m): 
                        continue
                    if (ti, tj) in visited:
                        continue

                    visited.add((ti,tj))
                    nq.append((ti, tj))
            count += 1
            q = nq 
    
        return count -1 
        



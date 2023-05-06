class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        dirs = [
            [1, 0], 
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        def is_island(i, j):
            nonlocal n, m
            if (i, j) in visited:
                return visited[(i,j)]

            path.add((i,j))

            island = True    
            for down, right in dirs:
                ti = i + down
                tj = j + right

                if not (0 <= ti < n and 0<= tj < m):
                    return False


                if grid[ti][tj] == 0 and (ti, tj) not in path:
                    if not is_island(ti, tj):
                        island = False


            path.remove((i,j))
            visited[(i,j)] = island
            return island


        count = 0
        visited = {}
        for i in range(n):
            for j in range(m):
                path = set()
                if grid[i][j] == 0 and (i,j) not in visited:
                    if is_island(i, j):
                        count += 1

        return count

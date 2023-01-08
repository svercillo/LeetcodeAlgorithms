class Counter:
    def __init__(self,):
        self.val = 0

    def count(self):
        self.val += 1

class Solution:

    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [] 
        for i in range(n):
            row = []
            for j in range(m):
                row.append(0)
            dp.append(row)

        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]

        
        visited = set()
        def dfs(i, j, counter, island_ind):
            nonlocal n, m
            
            if (i,j) in visited:
                return
            
            counter.count()
            dp[i][j] = island_ind

            visited.add((i,j))

            for _dir in directions:
                ti, tj = i + _dir[0], j + _dir[1]
                if 0 <= ti < n and 0 <= tj < m and grid[ti][tj] == 1:

                    dfs(ti, tj, counter, island_ind)
    
        island_sizes = {}
        island_ind = 0
        for i in range(n):
            for j in range(m):
                
                
                if grid[i][j]:
                    island_ind += 1
                    counter = Counter()
                    dfs(i, j, counter, island_ind)

                    island_sizes[island_ind] = counter.val
        if not len(island_sizes):
            return 1
        
        largest_island = max([island_sizes[_id] for _id in island_sizes])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    continue

                island_total = 0
                visited = set()
                for _dir in directions:
                    ti, tj = i + _dir[0], j + _dir[1]
                    if 0 <= ti < n and 0 <= tj < m and grid[ti][tj] == 1:
                        island_ind = dp[ti][tj]
                        if island_ind in visited:
                            continue
                        visited.add(island_ind)
                        island_total += island_sizes[island_ind]

                        # print(ti, tj, island_sizes[island_ind])

                res = max(res, island_total)

        print(island_sizes)
        print(dp)
        print(res)
        return max(res + 1, largest_island)

import math
class Solution:
    def shortestDistance(self, grid) -> int:
        
        
        n = len(grid)
        m = len(grid[0])
        
        
        houses = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    houses.append([i,j])
                    
        dp = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append([-1] * len(houses))
            dp.append(row)
            
        
        dirs = [ [1,0], [0,1], [-1,0], [0,-1]]
        def bfs(i, j, dpind):
            q = [(i,j)]

            dist = 0 
            while len(q):
                newq = []
                for i, j in q:                    
                    for up, right in dirs:
                        ti = i + up
                        tj = j + right
                    
                        if 0 <= ti < n and 0 <= tj < m and grid[ti][tj] == 0:
                            if dp[ti][tj][dpind] != -1: 
                                continue
                            else: # hasn't been visited yet
                                dp[ti][tj][dpind] = dist +1
                                newq.append([ti, tj])
                q = newq
                dist += 1
                
                    
        for dpind, house in enumerate(houses):
            bfs(*house, dpind)
            
        # from pprint import pprint
        # pprint(dp)


        smallest_sum  = math.inf

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    s = 0
                    skip = False
                    for dist in dp[i][j]: 
                        if dist == -1:
                            skip = True
                            break
                    if skip:
                        continue

                    smallest_sum = min(smallest_sum, sum(dp[i][j]))

        return smallest_sum if smallest_sum != math.inf else -1 

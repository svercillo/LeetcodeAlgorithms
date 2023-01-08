class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
                
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        n = len(grid)
        m = len(grid[0])
        
        

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "*":
                    starti = i
                    startj = j 
                    
                    
        
        q = [(starti, startj)]
                
            
        visited = set()
        steps = 0
        while len(q) > 0:
            
            new_q = []
            for i, j in q:
                
                if (i,j) in visited:
                    continue
                
                visited.add((i,j))
                
                for down, right in dirs:
                    ti = i + down
                    tj = j + right
                    
                    
                    if 0 <= ti < n and 0 <= tj < m and grid[ti][tj] in ["#", "O"]:
                        if grid[ti][tj] == "#":
                            return steps + 1
                        else:
                            new_q.append((ti,tj))
                            
                        
            q = new_q

            steps += 1

            
        return -1

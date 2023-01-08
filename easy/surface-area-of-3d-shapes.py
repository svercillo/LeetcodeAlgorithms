class Solution:
    def surfaceArea(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        
        if n ==m == 1: 
            return grid[0][0] * 4 + 2 
        
        sa = 0
        for i in range(n):
            for j in range(m):
                
                if i == 0 or i == n-1:
                    sa += grid[i][j] 
                    
                
                if j == 0 or j == m-1:
                    sa += grid[i][j]
                    
                
                if i - 1 >=0:
                    sa += abs(grid[i-1][j] - grid[i][j]) 
                    
                if j - 1 >= 0:
                    sa += abs(grid[i][j-1] - grid[i][j])
            
                
                if grid[i][j] > 0:
                    sa += 2 # for top and bottom 
                
        return sa

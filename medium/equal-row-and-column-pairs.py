class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        
        n = len(grid)
        m = len(grid[0])
        
        if n != m: 
            return 0
                                                                                                          
        for i in range(n):
            row = tuple(grid[i])
            if row not in rows:
                rows[row] = 0
            rows[row] += 1
            
            
            
        total = 0 
        for j in range(m):
            col = []
            
            for i in range(n):
                col.append(grid[i][j])
            
            col = tuple(col)
            if col in rows:
                total += rows[col]
                
        return total

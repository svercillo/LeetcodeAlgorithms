class Solution:
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        count =0     
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == '1':
                    count +=1
                    self.dfs(i, j)
        
        return count
        
    
    def dfs(self, i, j):
        if i < 0 or i >= len(self.grid):
            return
        elif j <0 or j >= len(self.grid[0]):
            return
        
    
        if self.grid[i][j] == '0':
            return 
        

        self.grid[i][j] = '0'
        
        self.dfs(i -1, j)
        self.dfs(i +1, j)
        self.dfs(i, j+1)       
        self.dfs(i, j-1)       
        
        
        
        
        
    

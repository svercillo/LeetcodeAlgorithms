class Solution:
    def knightProbability(self, n: int, num_moves: int, row: int, column: int) -> float:
        
        
        visited = {}
        
        moves = ((2, 1), (2, -1), (1, 2), (-1,2), (-2, 1), (-2, -1), (1, -2) , (-1, -2)) # (i,j )
        
        total = 0 
        def dfs(i, j, k):
            
            if (i, j, k) in visited:
                return visited[(i,j,k)]
            
            if i < 0 or i >= n or j < 0 or j >=n:
                return 0
            
            if k ==0:
                return 1
            
            
            total = 0
            for m in moves:
                res = dfs(i + m[0], j+m[1], k-1)
                
                total += 1/8 * res
                visited[(i + m[0], j+m[1], k-1)] = res
            
            return total
        
        
        res = dfs(row, column, num_moves)
        
        print(res)
        
        return res
                
            
            
            
            
            
            
            

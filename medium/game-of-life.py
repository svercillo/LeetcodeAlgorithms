class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
            
        dirs = []
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0: continue 
                dirs.append((i,j))
                
        
        # 10 represents 0 that was previously 1  Any live cell with fewer than two live neighbors dies as if caused by under-population.
        # 20 represents 1 that was previously 1  Any live cell with two or three live neighbors lives on to the next generation.
        # 30 represents 0 that was previously 1  Any live cell with more than three live neighbors dies, as if by over-population.
        # 40 represents 1 that was previously 0  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        
        for i in range(n):
            for j in range(m):
                prev = board[i][j]
                
                neigh = 0
                for d in dirs:
                    ti = i + d[0]
                    tj = j + d[1]
                    
                    
                    if 0 <= ti < n and 0 <= tj < m:
                        if (i, j) == (1, 0):
                            print(ti, tj, "AAAA", board[ti][tj])
                        if board[ti][tj] in [10, 20, 30, 1]:
                            neigh += 1
 
                if prev == 1 and neigh < 2: 
                    board[i][j] = 10
                elif prev == 1 and neigh in [2, 3]:
                    board[i][j] = 20
                elif prev == 1 and neigh > 3:
                    board[i][j] = 30
                elif prev == 0 and neigh == 3:
                    board[i][j] = 40
                    
            
        for i in range(n):
            for j in range(m):
                if board[i][j] in [20, 40, 1]:
                    board[i][j] = 1
                
                else:
                    board[i][j] = 0
                    
        return

                    
                        
                        
                        
                    
                    
                
                

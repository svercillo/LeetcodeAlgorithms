class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        n, m = len(board), len(board[0])

        dirs = []
        for down in range(-1, 2):
            for right in range(-1, 2):
                if down == right == 0:
                    continue 

                dirs.append([down, right])

        
        print(dirs)

        num_adj = {}    
        for i in range(n):
            for j in range(m):
                
                num_adj_mines = 0
                for down, right in dirs:
                    ti = i + down
                    tj = j + right

                    if (0 <= ti < n and 0 <= tj < m):
                        if board[ti][tj] == "M":
                            num_adj_mines += 1
                    
                num_adj[(i, j)] = num_adj_mines

        q = [click]

        while len(q):
            i, j = q.pop()


            if board[i][j] == "M":
                board[i][j] = "X"
                return board
            
            
            if (i, j) not in num_adj:
                continue

            if num_adj[(i, j)] != 0:
                board[i][j] = str(num_adj[(i,j)])
            else: 

                for down, right in dirs:
                    ti = i + down
                    tj = j + right

                    if (0 <= ti < n and 0 <= tj < m):
                        q.append((ti, tj))

                board[i][j] = "B"
                        
            num_adj.pop((i,j))
        

        return board

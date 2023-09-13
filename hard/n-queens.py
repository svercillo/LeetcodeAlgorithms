class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # idea: go column by column and backtrack 
        r_used = set()
        d_diag = set() # the y value of the downward diagonal at x = 0
        u_diag = set() # the y value of the upward diagonal at x = 0
        positions = []

        arrangements = []

        def dfs(col):
            nonlocal n
            if col == n:
                arrangements.append(positions.copy())
                return 0

            num_ways = 0
            for row in range(n):

                if row not in r_used and row - col not in d_diag and row + col not in u_diag:

                    r_used.add(row)
                    d_diag.add(row - col)
                    u_diag.add(row + col)
                    positions.append((row, col))

                    num_ways += dfs(col + 1)

                    positions.pop()
                    r_used.remove(row)
                    d_diag.remove(row - col) 
                    u_diag.remove(row + col)
            return num_ways

        dfs(0)

        def build_board(arrangement):
            nonlocal n

            board = [] 

            for i in range(n): 
                row = []
                for j in range(n):
                    row.append(".")
                board.append(row)


            for i, j in arrangement:a
                board[i][j] = "Q"

            return [ "".join(row) for row in board]

        return [build_board(arrange) for arrange in arrangements]



                



        print(arrangements)

        

            


            

            
            


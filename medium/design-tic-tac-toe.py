class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = []
        
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append(0)    
            self.board.append(row)
            
        self.diagonals = [[-1, 0], [-1, 0 ]]
        self.horiz = [[-1, 0] for _ in range(n)]
        self.verts = [[-1, 0] for _ in range(n)]
        
    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        
        # print(row, col, n, n-1 -row)
        
        possible = []
        if col == row:
            possible.append(self.diagonals[0])  
        if col == n -1 - row:
            possible.append(self.diagonals[1])
            print("A", row, col)
            print(possible[-1])
         
        possible.append(self.verts[row])
        possible.append(self.horiz[col])
        
        for option in possible:
            
            if option[1] == 0 or option[0] == player:
                option[0] = player
            
            else:
                option[0] = -1 # remove option from both = 
            option[1] += 1 

            if option[1] == n and option[0] == player:
                return player
                
                
        return 0
                
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

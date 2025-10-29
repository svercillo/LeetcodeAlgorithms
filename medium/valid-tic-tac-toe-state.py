
class Solution:
    def validTicTacToe(self, board):
        win = []
        numX, numO = 0, 0
        for i in range(3):
            cVal = board[i][0]
            rVal = board[0][i]
            
            invalidC = False
            invalidR = False
            for j in range(0, 3):
                if board[i][j] == "X":
                    numX += 1
                elif board[i][j] == "O": 
                    numO += 1

                if not (board[i][j] == cVal != " "):
                    invalidC = True
                    
                if not(board[j][i] == rVal != " "):
                    invalidR = True
                    
            if not invalidC:
                win.append(cVal)
            
            if not invalidR:
                win.append(rVal)
        
        invalidD1 = False
        invalidD2 = False
        d1Val = board[0][0]
        d2Val = board[0][2]
        for i in range(3):
            if not (board[i][i] == d1Val  != " "):
                invalidD1 = True
                
            if not(board[i][2-i] == d2Val != " "): 
                invalidD2 = True
                
        if not invalidD1:
            win.append(d1Val)
            
        if not invalidD2: 
            win.append(d2Val)
            
        if len(win) == 2 and (win[0] != win[1] or win[0] == "O"):
            return False
        
        if numX > numO:
            if numX - numO > 1:
                return False
            
            if len(win) and win[0] == "O":
                return False

        elif numX < numO:
            return False
        
        else:
            if len(win) and win[0] == "X":
                return False
        
        return True        
                

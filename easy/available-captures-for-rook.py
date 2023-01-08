class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = len(board)
        b = board
        
        count = 0
        _i =0
        _j =0 
        for i in range(n):
            for j in range(n):
                if b[i][j] == "R":
                    _i = i
                    _j = j
                    break
        
        ic = _i
        
        while ic >= 0:
            if b[ic][_j] == "B": break
            elif b[ic][_j] == "p": 
                count += 1
                break
            ic -=1
            
        ic = _i
        while ic < n:
            if b[ic][_j] == "B": break
            elif b[ic][_j] == "p": 
                print(ic, _j)
                count += 1
                break 
            ic +=1

        
        jc = _j
        while jc >= 0:
            if b[_i][jc] == "B": break
            elif b[_i][jc] == "p": 
                count += 1
                break
            jc -=1
            
        jc = _j
        while jc < n:
            if b[_i][jc] == "B": break
            elif b[_i][jc] == "p":
                count += 1
                break
            jc +=1
            
        
        return count 
            
        
            

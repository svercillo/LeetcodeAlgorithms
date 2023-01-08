class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    
        n = len(mat)
        m = len(mat[0])
        
        if n * m != r * c:
            return mat
        
        
        row = 0
        col = 0
        
        res = []
        curr = []
        i = 0
        while i < m * n:
            # print(i, row, col)
            curr.append(mat[row][col])
            if (i +1) % c == 0:
                res.append(curr)
                curr = []

            if (i+1) % m == 0: 
                row +=1 
                col = -1
                
            

            
            col +=1 
            i +=1
            
        return res

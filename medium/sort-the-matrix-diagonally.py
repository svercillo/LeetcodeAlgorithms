class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        
        for i in range(m):
            
            
            diag = []
            col = i
            row = 0
            while col < m and row <n: 
                diag.append(mat[row][col])
                col += 1
                row += 1 
            
            diag.sort()
            
            
            col = i
            row = 0
            c = 0
            while col < m and row <n: 
                mat[row][col] = diag[c]
                col += 1
                row += 1
                c +=1
        
        for i in range(1, n):    
            
            diag = []
            col = 0
            row = i
            while col < m and row <n: 
                diag.append(mat[row][col])
                col += 1
                row += 1 
            

            diag.sort()
            
            col = 0
            row = i
            c = 0
            while col < m and row <n: 
                mat[row][col] = diag[c]
                row += 1 
                col += 1
                c +=1
        
        return mat 
            
            

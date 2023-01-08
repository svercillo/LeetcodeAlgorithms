class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        
        res = []
        for j in range(m):
            row = []
            for i in range(n):
                row.append(matrix[i][j])
            res.append(row)
            
        return res
            
                
                
            
